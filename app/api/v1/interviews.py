from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, require_roles
from app.core.database import get_db
from app.models.application import Application
from app.models.candidate import Candidate
from app.models.interview import Interview
from app.schemas.interview import InterviewCreate, InterviewUpdate, InterviewResponse
from app.services.email_service import EmailService
from app.services.google_calendar_service import GoogleCalendarService

router = APIRouter(prefix="/api/v1/interviews", tags=["Interviews"])


@router.get("/", response_model=list[InterviewResponse])
def get_interviews(db: Session = Depends(get_db), _=Depends(get_current_user)):
    return db.query(Interview).all()


@router.get("/{interview_id}", response_model=InterviewResponse)
def get_interview(interview_id: int, db: Session = Depends(get_db), _=Depends(get_current_user)):
    interview = db.query(Interview).filter(Interview.id == interview_id).first()
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")
    return interview


@router.post("/", response_model=InterviewResponse)
async def create_interview(
    payload: InterviewCreate,
    db: Session = Depends(get_db),
    _=Depends(require_roles("admin", "hr"))
):
    application = db.query(Application).filter(Application.id == payload.application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    candidate = db.query(Candidate).filter(Candidate.id == application.candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    calendar_result = await GoogleCalendarService.create_event(
        summary=f"Interview - {candidate.full_name}",
        start_time=payload.start_time,
        end_time=payload.end_time,
        attendees=[candidate.email]
    )

    interview = Interview(
        application_id=payload.application_id,
        interviewer_id=payload.interviewer_id,
        schedule_time=datetime.fromisoformat(payload.start_time),
        end_time=datetime.fromisoformat(payload.end_time),
        location=payload.location,
        meeting_link=calendar_result.get("meeting_link"),
        type=payload.type,
        status="scheduled"
    )
    db.add(interview)
    db.commit()
    db.refresh(interview)

    EmailService.send_email(
        to_email=candidate.email,
        subject="Interview Invitation",
        body=(
            f"Xin chào {candidate.full_name},\n\n"
            f"Bạn được mời tham gia phỏng vấn.\n"
            f"Thời gian: {payload.start_time}\n"
            f"Link họp: {interview.meeting_link}\n"
        )
    )

    return interview


@router.put("/{interview_id}", response_model=InterviewResponse)
def update_interview(
    interview_id: int,
    payload: InterviewUpdate,
    db: Session = Depends(get_db),
    _=Depends(require_roles("admin", "hr", "interviewer"))
):
    interview = db.query(Interview).filter(Interview.id == interview_id).first()
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(interview, key, value)

    db.commit()
    db.refresh(interview)
    return interview


@router.delete("/{interview_id}")
def delete_interview(
    interview_id: int,
    db: Session = Depends(get_db),
    _=Depends(require_roles("admin", "hr"))
):
    interview = db.query(Interview).filter(Interview.id == interview_id).first()
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")

    db.delete(interview)
    db.commit()
    return {"message": "Interview deleted"}
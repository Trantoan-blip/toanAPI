from fastapi import APIRouter, Depends
from app.api.deps import require_roles
from app.schemas.integration import (
    LinkedInImportRequest,
    LinkedInPublishJobRequest,
    EmailSendRequest,
    CalendarCreateEventRequest,
)
from app.services.linkedin_service import LinkedInService
from app.services.email_service import EmailService
from app.services.google_calendar_service import GoogleCalendarService

router = APIRouter(prefix="/api/v1/integrations", tags=["Integrations"])


@router.post("/linkedin/import-profile")
async def import_profile(
    payload: LinkedInImportRequest,
    _=Depends(require_roles("admin", "hr"))
):
    return await LinkedInService.import_profile(payload.profile_id)


@router.post("/linkedin/publish-job")
async def publish_job(
    payload: LinkedInPublishJobRequest,
    _=Depends(require_roles("admin", "hr"))
):
    return await LinkedInService.publish_job(payload.model_dump())


@router.post("/email/send")
def send_email(
    payload: EmailSendRequest,
    _=Depends(require_roles("admin", "hr"))
):
    return EmailService.send_email(payload.to_email, payload.subject, payload.body)


@router.post("/calendar/create-event")
async def create_event(
    payload: CalendarCreateEventRequest,
    _=Depends(require_roles("admin", "hr"))
):
    return await GoogleCalendarService.create_event(
        summary=payload.summary,
        start_time=payload.start_time,
        end_time=payload.end_time,
        attendees=[str(email) for email in payload.attendees]
    )
from pydantic import BaseModel
from typing import Optional


class InterviewCreate(BaseModel):
    application_id: int
    interviewer_id: int
    start_time: str
    end_time: str
    location: Optional[str] = None
    type: str = "online"


class InterviewUpdate(BaseModel):
    location: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    feedback: Optional[str] = None


class InterviewResponse(BaseModel):
    id: int
    application_id: int
    interviewer_id: int
    location: Optional[str]
    meeting_link: Optional[str]
    type: str
    status: str
    feedback: Optional[str]

    class Config:
        from_attributes = True
from pydantic import BaseModel, EmailStr
from typing import Optional


class LinkedInImportRequest(BaseModel):
    profile_id: str


class LinkedInPublishJobRequest(BaseModel):
    title: str
    description: str
    location: Optional[str] = None


class EmailSendRequest(BaseModel):
    to_email: EmailStr
    subject: str
    body: str


class CalendarCreateEventRequest(BaseModel):
    summary: str
    start_time: str
    end_time: str
    attendees: list[EmailStr]
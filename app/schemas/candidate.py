from pydantic import BaseModel, EmailStr
from typing import Optional


class CandidateCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    linkedin_url: Optional[str] = None
    cv_url: Optional[str] = None
    skills: Optional[str] = None
    experience_years: int = 0


class CandidateUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    linkedin_url: Optional[str] = None
    cv_url: Optional[str] = None
    skills: Optional[str] = None
    experience_years: Optional[int] = None
    status: Optional[str] = None


class CandidateResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: Optional[str]
    linkedin_url: Optional[str]
    cv_url: Optional[str]
    skills: Optional[str]
    experience_years: int
    status: str

    class Config:
        from_attributes = True
from pydantic import BaseModel
from typing import Optional


class ApplicationCreate(BaseModel):
    candidate_id: int
    job_id: int
    source: Optional[str] = None
    note: Optional[str] = None


class ApplicationUpdate(BaseModel):
    status: Optional[str] = None
    source: Optional[str] = None
    note: Optional[str] = None


class ApplicationResponse(BaseModel):
    id: int
    candidate_id: int
    job_id: int
    status: str
    source: Optional[str]
    note: Optional[str]

    class Config:
        from_attributes = True
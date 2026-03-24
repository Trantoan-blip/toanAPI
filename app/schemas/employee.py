from pydantic import BaseModel
from typing import Optional
from datetime import date


class EmployeeCreate(BaseModel):
    candidate_id: Optional[int] = None
    employee_code: str
    department: Optional[str] = None
    position: Optional[str] = None
    hire_date: Optional[date] = None
    contract_type: Optional[str] = None
    status: str = "active"


class EmployeeUpdate(BaseModel):
    department: Optional[str] = None
    position: Optional[str] = None
    hire_date: Optional[date] = None
    contract_type: Optional[str] = None
    status: Optional[str] = None


class EmployeeResponse(BaseModel):
    id: int
    candidate_id: Optional[int]
    employee_code: str
    department: Optional[str]
    position: Optional[str]
    hire_date: Optional[date]
    contract_type: Optional[str]
    status: str

    class Config:
        from_attributes = True
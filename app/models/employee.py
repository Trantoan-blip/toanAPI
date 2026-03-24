from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.core.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    employee_code = Column(String(50), unique=True, nullable=False)
    department = Column(String(100))
    position = Column(String(100))
    hire_date = Column(Date)
    contract_type = Column(String(50))
    status = Column(String(50), default="active")
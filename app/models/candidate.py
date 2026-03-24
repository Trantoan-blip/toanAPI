from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    phone = Column(String(20))
    linkedin_url = Column(String(255))
    cv_url = Column(String(255))
    skills = Column(Text)
    experience_years = Column(Integer, default=0)
    status = Column(String(50), default="new")
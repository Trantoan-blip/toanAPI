from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.core.database import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.id"), nullable=False)
    interviewer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    schedule_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String(255))
    meeting_link = Column(String(255))
    type = Column(String(50), default="online")
    status = Column(String(50), default="scheduled")
    feedback = Column(String(1000))
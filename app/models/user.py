from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    about = relationship("About", uselist=False, back_populates="user")
    skills = relationship("Skill", back_populates="user")
    achievements = relationship("Achievement", back_populates="user")
    languages = relationship("Language", back_populates="user")
    projects = relationship("Project", back_populates="user")
    contact = relationship("Contact", uselist=False, back_populates="user")

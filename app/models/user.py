from sqlalchemy import Column, String, Boolean, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())
    email = Column(String, unique=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column("isActive",Boolean, nullable=False, server_default=func.true())
    created_at = Column("createdAt", DateTime, server_default=func.now(), nullable=False)
    updated_at = Column("updatedAt", DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    projects = relationship("Project", back_populates="user")
    about = relationship("About", uselist=False, back_populates="user")
    languages = relationship("Language", back_populates="user")
    achievements = relationship("Achievement", back_populates="user", cascade="all, delete-orphan")
    contact = relationship("Contact", uselist=False, back_populates="user")
    skills = relationship("Skill", back_populates="user")

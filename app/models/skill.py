from sqlalchemy import Column, String, Enum, ForeignKey, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import enum

from app.db.session import Base


class SkillCategory(str, enum.Enum):
    LANGUAGES = "languages"
    FRONTEND = "frontend"
    BACKEND = "backend"
    DATABASES = "databases"
    DEVOPS = "devops"
    INTEGRATIONS = "integrations"
    PRACTICES = "practices"


class Skill(Base):
    __tablename__ = "skills"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String, nullable=False)
    category = Column(Enum(SkillCategory), default=SkillCategory.PRACTICES, nullable=False)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="skills")

    # Relaciones inversas desde Project y Contact (si las tenés)
    projects = relationship("Project", secondary="project_skills", back_populates="technologies")
    contact_opportunities = relationship("Contact", secondary="contact_opportunities", back_populates="opportunities")
    contact_location_info = relationship("Contact", secondary="contact_location_info", back_populates="location_info")

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

from sqlalchemy import Column, String, Enum, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import enum

from app.db.session import Base


class SkillCategory(str, enum.Enum):
    languages = "languages"
    frontend = "frontend"
    backend = "backend"
    databases = "databases"
    devops = "devops"
    integrations = "integrations"
    practices = "practices"


class Skill(Base):
    __tablename__ = "skills"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())

    name = Column(String, nullable=False)

    category = Column(
    Enum(SkillCategory, name="skills_category_enum", create_type=False),
    server_default=SkillCategory.practices.value,
    nullable=False,
)

    user_id = Column("userId",UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="skills")

    project_skills = relationship("ProjectSkill", back_populates="skill")
    contact_opportunities = relationship("ContactOpportunity", back_populates="skill")
    contact_location_info = relationship("ContactLocationInfo", back_populates="skill")


    created_at = Column("createdAt", DateTime, server_default=func.now(), nullable=False)
    updated_at = Column("updatedAt", DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

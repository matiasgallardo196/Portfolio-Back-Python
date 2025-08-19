from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.session import Base


class ProjectSkill(Base):
    __tablename__ = "project_skills"

    project_id = Column("projectId", UUID(as_uuid=True), ForeignKey("projects.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    skill_id = Column("skillId", UUID(as_uuid=True), ForeignKey("skills.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)

    project = relationship("Project", back_populates="project_skills")
    skill = relationship("Skill", back_populates="project_skills")

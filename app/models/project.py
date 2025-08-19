from sqlalchemy import Column, String, Text, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


from app.db.session import Base



class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())

    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    github_url = Column("githubUrl",String, nullable=False)
    demo_url = Column("demoUrl",String, nullable=True)
    image_url = Column("imageUrl",String, nullable=False)

    user_id = Column("userId",UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="projects")

    project_skills = relationship("ProjectSkill", back_populates="project")

    created_at = Column("createdAt", DateTime, server_default=func.now(), nullable=False)
    updated_at = Column("updatedAt", DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

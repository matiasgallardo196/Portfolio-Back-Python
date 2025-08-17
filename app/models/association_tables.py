from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base

project_skills = Table(
    "project_skills", Base.metadata,
    Column("project_id", UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True),
    Column("skill_id", UUID(as_uuid=True), ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True),
)
contact_opportunities = Table(
    "contact_opportunities", Base.metadata,
    Column("contact_id", UUID(as_uuid=True), ForeignKey("contact.id", ondelete="CASCADE"), primary_key=True),
    Column("skill_id", UUID(as_uuid=True), ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True),
)
contact_location_info = Table(
    "contact_location_info", Base.metadata,
    Column("contact_id", UUID(as_uuid=True), ForeignKey("contact.id", ondelete="CASCADE"), primary_key=True),
    Column("skill_id", UUID(as_uuid=True), ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True),
)

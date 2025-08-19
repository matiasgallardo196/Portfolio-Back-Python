from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.session import Base


class ContactLocationInfo(Base):
    __tablename__ = "contact_location_info"

    contact_id = Column("contactId", UUID(as_uuid=True), ForeignKey("contact.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    skill_id = Column("skillId", UUID(as_uuid=True), ForeignKey("skills.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)

    contact = relationship("Contact", back_populates="location_info")
    skill = relationship("Skill", back_populates="contact_location_info")

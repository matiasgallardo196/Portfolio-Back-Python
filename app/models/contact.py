from sqlalchemy import Column, String, Text, ForeignKey, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.models.association_tables import contact_opportunities, contact_location_info


from app.db.session import Base

class Contact(Base):
    __tablename__ = "contact"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    email = Column(String, nullable=False)
    linkedin = Column(String, nullable=False)
    github = Column(String, nullable=False)
    whatsapp = Column(String, nullable=True)
    meta_description = Column(String, nullable=False)
    page_title = Column(String, nullable=False)
    hero_title = Column(String, nullable=False)
    lets_talk_title = Column(String, nullable=False)
    lets_talk_description = Column(Text, nullable=False)
    availability_title = Column(String, nullable=False)
    current_status_title = Column(String, nullable=False)
    location_title = Column(String, nullable=False)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)
    user = relationship("User", back_populates="contact", uselist=False)

    opportunities = relationship("Skill", secondary=contact_opportunities, backref="opportunity_contacts")
    locationInfo = relationship("Skill", secondary=contact_location_info, backref="location_contacts")


    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

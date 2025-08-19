from sqlalchemy import Column, String, Text, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


from app.db.session import Base

class Contact(Base):
    __tablename__ = "contact"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())

    email = Column(String, nullable=False)
    linkedin = Column(String, nullable=False)
    github = Column(String, nullable=False)
    whatsapp = Column(String, nullable=True)
    meta_description = Column("metaDescription",String, nullable=False)
    page_title = Column("pageTitle",String, nullable=False)
    hero_title = Column("heroTitle",String, nullable=False)
    lets_talk_title = Column("letsTalkTitle",String, nullable=False)
    lets_talk_description = Column("letsTalkDescription",Text, nullable=False)
    availability_title = Column("availabilityTitle",String, nullable=False)
    current_status_title = Column("currentStatusTitle",String, nullable=False)
    location_title = Column("locationTitle",String, nullable=False)

    user_id = Column("userId",UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)
    user = relationship("User", back_populates="contact", uselist=False)

    opportunities = relationship("ContactOpportunity", back_populates="contact", cascade="all, delete-orphan")
    location_info = relationship("ContactLocationInfo", back_populates="contact", cascade="all, delete-orphan")


    created_at = Column("createdAt", DateTime, server_default=func.now(), nullable=False)
    updated_at = Column("updatedAt", DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

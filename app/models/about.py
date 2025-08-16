from sqlalchemy import Column, String, Text, ForeignKey, JSON, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.db.session import Base


class About(Base):
    __tablename__ = "about"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    full_name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    biography = Column(Text, nullable=False)
    page_description = Column(String, nullable=False)
    meta_description = Column(String, nullable=False)
    hero_title = Column(String, nullable=False)
    hero_subtitle = Column(String, nullable=False)
    avatar_url = Column(String, nullable=False)
    relocation_status = Column(String, nullable=False)

    cta_buttons = Column(JSON, nullable=False)
    stats = Column(JSON, nullable=False)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    user = relationship("User", back_populates="about", uselist=False)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

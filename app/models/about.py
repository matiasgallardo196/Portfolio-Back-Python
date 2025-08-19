from sqlalchemy import Column, String, Text, ForeignKey, JSON, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.session import Base


class About(Base):
    __tablename__ = "about"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())
    
    full_name = Column("fullName",String, nullable=False)
    location = Column(String, nullable=False)
    biography = Column(Text, nullable=False)
    page_description = Column("pageDescription",String, nullable=False)
    meta_description = Column("metaDescription",String, nullable=False)
    hero_title = Column("heroTitle",String, nullable=False)
    hero_subtitle = Column("heroSubtitle",String, nullable=False)
    avatar_url = Column("avatarUrl",String, nullable=False)
    relocation_status = Column("relocationStatus",String, nullable=False)

    cta_buttons = Column("ctaButtons",JSON, nullable=False)
    stats = Column(JSON, nullable=False)

    user_id = Column("userId",UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    user = relationship("User", back_populates="about", uselist=False)

    created_at = Column("createdAt", DateTime, server_default=func.now(), nullable=False)
    updated_at = Column("updatedAt", DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

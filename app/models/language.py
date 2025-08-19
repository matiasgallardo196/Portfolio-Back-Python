from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.session import Base


class Language(Base):
    __tablename__ = "languages"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())

    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    is_native = Column("isNative", Boolean,nullable=False, server_default=func.false())

    user_id = Column("userId",UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="languages")

    created_at = Column("createdAt", DateTime, server_default=func.now(), nullable=False)
    updated_at = Column("updatedAt", DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

from sqlalchemy import Column, Integer, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class StylistSlot(Base):
    __tablename__ = "stylist_slot"

    id = Column(Integer, primary_key=True)
    slot_num = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    waiting = relationship("Waiting", back_populates="slot")
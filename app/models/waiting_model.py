from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
from app.core.enums import WaitingStatus

class Waiting(Base):
    __tablename__ = "waiting"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)

    status = Column(Enum(WaitingStatus), nullable=False)
    queue_order = Column(Integer, nullable=False)

    slot_id = Column(Integer, ForeignKey("stylist_slot.id"), nullable=True)

    estimated_minutes = Column(Integer, nullable=False, default=15)
    started_at = Column(DateTime(timezone=True), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    customer = relationship("Customer", back_populates="waiting")
    slot = relationship("StylistSlot", back_populates="waiting")
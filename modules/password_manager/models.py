import uuid
from typing import Optional
from datetime import datetime, timezone

from sqlalchemy import DateTime, Text, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


class PasswordRecord(Base, TimestampMixin):
    __tablename__ = "passwords"

    id: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid.uuid4()), primary_key=True)
    name: Mapped[str] = mapped_column(String(75), nullable=False, index=True)
    username: Mapped[str] = mapped_column(String(75), nullable=False)
    password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    url: Mapped[Optional[str]] = mapped_column(Text)
    # crypto metadata #! TO CHANGE
    salt: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    nonce: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

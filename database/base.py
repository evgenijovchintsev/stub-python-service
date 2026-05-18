"""SQLAlchemy declarative base and common model mixin.

Provides a reusable :class:`Base` for ORM model definitions and a ``BaseModel``
Mixin that adds an integer primary key ``id`` and timestamp columns
``created_at`` and ``updated_at``.
"""

from __future__ import annotations

import datetime

from sqlalchemy import DateTime, Integer, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for all ORM models."""
    # No additional attributes needed; inherits from DeclarativeBase.


class BaseModel:
    """Mixin adding ``id``, ``created_at`` and ``updated_at`` columns.

    Models can inherit from both ``Base`` and ``BaseModel`` (or just
    ``BaseModel`` if they already extend a custom ``Base``). The ``id`` field
    is an auto‑incrementing primary key. ``created_at`` is set to the current
    UTC time on insert, and ``updated_at`` is refreshed on each update.
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now,  # avoid lint error by passing the callable without invoking it
        nullable=False,
    )

}
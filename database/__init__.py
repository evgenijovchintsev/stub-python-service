"""Database package initialization.

Exports the declarative ``Base`` and the ``BaseModel`` mixin for ORM models.
"""

from .base import Base, BaseModel

__all__ = ["Base", "BaseModel"]

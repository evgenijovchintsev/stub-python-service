"""Example ORM models inheriting from the common Base.

The project currently contains only the base class.  Adding a concrete model
helps illustrate how user‑defined tables should be defined and guarantees that
``Base.metadata`` will contain at least one table for Alembic autogeneration.
"""

from sqlalchemy import Column, Integer, String
from database import Base

class Example(Base):
    """A minimal example table used only for illustration.

    The class inherits ``Base`` which already provides the ``id``,
    ``created_at`` and ``updated_at`` columns.  Only an additional ``name``
    column is declared here.
    """

    __tablename__ = "examples"
    name = Column(String(100), nullable=False)

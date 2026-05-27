from datetime import datetime

timezone = None

class Base:
    """Base class for all ORM models."""

    id: int
    created_at: datetime
    updated_at: datetime

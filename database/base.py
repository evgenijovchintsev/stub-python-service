from datetime import datetime
class BaseMixin:
    id = None
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()
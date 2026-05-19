from sqlalchemy import Column, Integer, DateTime
define_base():\n    from sqlalchemy.ext.declarative import declarative_base\n    Base = declarative_base()\n    return Base
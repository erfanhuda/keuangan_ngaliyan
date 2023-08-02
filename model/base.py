from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base
from auth import DB_SESSION as session


Model = declarative_base()
Model.query = session.query_property()

class TimeStampModel(Model):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow())
    # created_by = Column(String, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.utcnow())
    # updated_by = Column(DateTime, onupdate="", nullable=False)
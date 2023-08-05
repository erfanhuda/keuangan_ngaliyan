from datetime import datetime
from sqlalchemy import Column, DateTime, Table, String
from sqlalchemy.orm import declarative_base
from auth import DB_SESSION as session, DB_ENGINE as engine


Model = declarative_base()
Model.query = session.query_property()

class TimeStampModel(Model):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow())
    created_by = Column(String(255), nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.utcnow())
    updated_by = Column(String(255), onupdate="", nullable=False)

class SchemaDBO(TimeStampModel):
    __abstract__ = True
    # __table_args__ = {"schema": "dbo"}

    pass
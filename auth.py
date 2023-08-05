import pathlib
import base64
import random
import os

from sqlalchemy import create_engine, event, Engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dataclasses import dataclass

@dataclass
class Auth:
    name: str
    auth_key: str
    auth_key_expired: str
    datetime: str

BASE_DIR = pathlib.Path(__file__)

# DB_ENGINE = create_engine(f"sqlite:///{BASE_DIR.parent}/data/db", echo=True)

try:
    DB_ENGINE = create_engine(f"mysql+pymysql://erfa6313_admin:Erfnhd100%@203.175.8.110/erfa6313_erfanhuda?charset=utf8mb4", echo=True)

    DB_SESSION = scoped_session(sessionmaker(autoflush=False, bind=DB_ENGINE))

    print("Connection successful")

    @event.listens_for(Engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        # cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

except ConnectionError as e:
    print("Error occurred")


# api/database.py
"""
database.py

This module contains the database configuration for the application.

Attributes:
SQLALCHEMY_DATABASE_URL (str): The database URL.
engine (sqlalchemy.engine.base.Engine): The database engine.
SessionLocal (sqlalchemy.orm.session.Session): The local database session.
Base (sqlalchemy.ext.declarative.api.DeclarativeMeta): The declarative base for ORM models.

"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./addresses.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

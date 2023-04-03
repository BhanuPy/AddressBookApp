# api/models.py
"""
models.py
Here we have define the structure for Address Table

Args:
    Base : The declarative base for ORM models.

Attributes:
    __tablename__ (str): The table name.
    id : The primary key column.
    address : The address column.
    latitude : The latitude column.
    longitude : The longitude column.

"""

from sqlalchemy import Column, Integer, String, Float
from api.database import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)

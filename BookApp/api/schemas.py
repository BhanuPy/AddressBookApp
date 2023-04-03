# api/schemas.py

"""
schemas.py

This module contains Pydantic schema classes for working with address data in the API.

"""
from typing import Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    """
    AddressBase: Base class defining fields for address data.
    """
    address: str
    latitude: float
    longitude: float


class AddressCreate(AddressBase):
    """
    Pydantic model for creating new address data.
    """
    pass


class AddressUpdate(AddressBase):
    """
    Pydantic model for updating existing address data.
    """
    id: int


class Address(AddressBase):
    """
    Pydantic model for returning address data from the API.
    """
    id: int

    class Config:
        orm_mode = True

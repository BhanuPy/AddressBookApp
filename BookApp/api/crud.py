#api/crud.py
"""
crud.py

Module for CRUD operations on Address table.

Contains class `AddressCRUD` with methods to create, read, update and delete addresses from the database.
"""

from typing import List
from sqlalchemy.orm import Session
from api.models import Address
from api.schemas import AddressCreate, AddressUpdate


class AddressCRUD:
    """
    class AddressCRUD with methods to create, read, update and delete addresses from the database.
    """
    def __init__(self, session: Session):
        self.session = session

    #Creates a new address in the database and returns the created address.
    def create_address(self, address: AddressCreate) -> Address:
        db_address = Address(**address.dict())
        self.session.add(db_address)
        self.session.commit()
        self.session.refresh(db_address)
        return db_address

    #Returns the address from the database with the given id.
    def get_address(self, address_id: int) -> Address:
        return self.session.query(Address).filter(Address.id == address_id).first()

    #Returns a list of all addresses in the database.
    def get_all_addresses(self) -> List[Address]:
        return self.session.query(Address).all()

    #Updates the address in the database with the given id and returns the updated address.
    def update_address(self, address: AddressUpdate) -> Address:
        db_address = self.get_address(address.id)
        db_address.address = address.address
        db_address.latitude = address.latitude
        db_address.longitude = address.longitude
        self.session.commit()
        self.session.refresh(db_address)
        return db_address

    #Deletes the address from the database with the given id.
    def delete_address(self, address_id: int):
        db_address = self.get_address(address_id)
        self.session.delete(db_address)
        self.session.commit()
        return  True

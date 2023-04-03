"""
This module defines API routes for managing addresses in the database.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlalchemy.orm import Session
from api.schemas import AddressCreate, AddressUpdate, Address
from api.crud import AddressCRUD
from api.database import SessionLocal, engine, Base
from utils.utils import get_distance



Base.metadata.create_all(bind=engine)

#addresses_router: A FastAPI router instance for defining the address routes.
addresses_router = APIRouter()

#Function to create a new database session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Endpoint to create a new address record in the database.
@addresses_router.post("/create_address/", response_model=Address)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    address_crud = AddressCRUD(db)
    db_address = address_crud.create_address(address)
    return db_address


#Endpoint to read an existing address record from the database.
@addresses_router.get("/get_address/{address_id}", response_model=Address)
def read_address(address_id: int, db: Session = Depends(get_db)):
    address_crud = AddressCRUD(db)
    db_address = address_crud.get_address(address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


#Endpoint to read all existing address records from the database.
@addresses_router.get("/get_all_addresses/", response_model=List[Address])
def read_addresses(db: Session = Depends(get_db)):
    address_crud = AddressCRUD(db)
    db_addresses = address_crud.get_all_addresses()
    return db_addresses


#Endpoint to update an existing address record in the database.
@addresses_router.post("/update_address/{address_id}", response_model=Address)
def update_address(address_id: int, address: AddressUpdate, db: Session = Depends(get_db)):
    address_crud = AddressCRUD(db)
    db_address = address_crud.get_address(address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    updated_address = address_crud.update_address(address)
    return updated_address


#Endpoint to delete an existing address record from the database.
@addresses_router.delete("/delete_address/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address_crud = AddressCRUD(db)
    db_address = address_crud.get_address(address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    is_deleted  = address_crud.delete_address(address_id)
    if is_deleted:
        return f"Address with id {address_id} has been deleted."
    


#Endpoint to get all addresses within a certain distance from a given latitude and longitude.
@addresses_router.get("/get_address/within/")
def get_addresses_within_distance(
    latitude: float = Query(..., ge=-90, le=90),
    longitude: float = Query(..., ge=-180, le=180),
    distance: float = Query(..., gt=0),
    db: Session = Depends(get_db),
):
    address_crud = AddressCRUD(db)
    db_addresses = address_crud.get_all_addresses()
    filtered_addresses = []
    for db_address in db_addresses:
        dist = get_distance(
            latitude, longitude, db_address.latitude, db_address.longitude
        )
        if dist <= distance:
            filtered_addresses.append(db_address)
    return filtered_addresses

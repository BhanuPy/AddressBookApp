# main.py

"""
# main.py

This module sets up a FastAPI application that includes a router for managing addresses. 
The code creates a new FastAPI application and attaches the `addresses_router` to it using the `include_router` method.
This allows the application to handle requests to URLs that start with:
 
 A) /create_address/ 
 B) /get_address/ 
 C) /get_all_addresses/ 
 D) /update_address/ 
 E) /delete_address/
 F) /get_address/within/

The code then runs the application using the Uvicorn server. 
Uvicorn is a high-performance ASGI server that can serve web applications built on top of ASGI-compatible frameworks like FastAPI.

This script is designed to be run directly using `python app.py`, which starts the server on `localhost:8000`.


"""
import uvicorn
from fastapi import FastAPI
from api.database import engine, Base
from api.routers.addresses import addresses_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(addresses_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

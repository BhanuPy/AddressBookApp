# AddressBookApp

Assignment
Create an address book application where API users can create, update and delete
addresses.
The address should:
- contain the coordinates of the address.
- be saved to an SQLite database.
- be validated

API Users should also be able to retrieve the addresses that are within a given distance and
location coordinates.
Important: The application does not need a GUI. (Built-in FastAPI’s Swagger Doc is sufficient)

-----------------------------------------------------------------------------------------------

Steps to run the AddressBookApp

1) Goto terminal
2) git clone https://github.com/BhanuPy/AddressBookApp.git
3) go inside the clone repository
4) create python virtual environment by command : py -m venv fastapienv
5) activate the fastapienv
6) go inside the BookApp folder
7) pip install - r requirements.txt #installing dependecies for the project
8) uvicorn main:app --reload #command to run the app
9) Open the browser
10) type and enter: http://localhost:8000/docs


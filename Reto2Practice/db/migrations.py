import os, sys
from peewee import SqliteDatabase
import time

# Add the parent directory of the 'schemas' folder to the Python path
schemas_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(schemas_path)

# Now you can import the modules from the 'schemas' folder
from schemas.user import User
from schemas.account import Account
from schemas.card import Card

def create_db(path: str):
    if not os.path.isfile(path):
        print(f"Creating database at path: {path}")
        db = SqliteDatabase(path)
        time.sleep(1)
        db.create_tables([User, Account, Card])
        print("Database created successfully.")
        return True
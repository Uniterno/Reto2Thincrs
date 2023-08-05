import os, sys
from peewee import SqliteDatabase
import time

# Now you can import the modules from the 'schemas' folder
from schemas.user import User
from schemas.account import Account
from schemas.card import Card
from schemas.charge import Charge
from schemas.payment import Payment


def create_db(path: str):
    if not os.path.isfile(path):
        print(f"Creating database at path: {path}")
        db = SqliteDatabase(path)
        time.sleep(1)
        db.create_tables([User, Account, Card, Charge, Payment])
        print("Database created successfully.")
        return True

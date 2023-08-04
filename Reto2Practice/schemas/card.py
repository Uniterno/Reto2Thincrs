from peewee import *
from schemas.account import Account

db = SqliteDatabase('./db/db_oltp.db', timeout=10)

class Card(Model):
    account_id = ForeignKeyField(Account, backref='cards')
    name = CharField()
    cvv = CharField(max_length=3)
    
    class Meta:
        database = db

from peewee import *
from schemas.account import Account

db = SqliteDatabase('./db/db_oltp.db', timeout=10)


class Payment(Model):
    account_id = ForeignKeyField(Account, backref='payment')
    date_time = DateField()
    amount = FloatField()

    class Meta:
        database = db

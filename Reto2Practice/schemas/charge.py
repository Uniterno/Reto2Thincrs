from peewee import *
from schemas.card import Card

db = SqliteDatabase('./db/db_oltp.db', timeout=10)


class Charge(Model):
    card_id = ForeignKeyField(Card, backref='charges')
    date_time = DateField()
    amount = FloatField()

    class Meta:
        database = db

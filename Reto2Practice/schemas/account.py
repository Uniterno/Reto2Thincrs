from peewee import *
from schemas.user import User

db = SqliteDatabase('./db/db_oltp.db', timeout=10)

class Account(Model):
    user_id = ForeignKeyField(User, backref='accounts')
    balance = FloatField()
    open_date = DateField()
    limit = FloatField()

    class Meta:
        database = db

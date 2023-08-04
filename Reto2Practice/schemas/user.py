from peewee import *

db = SqliteDatabase('./db/db_oltp.db', timeout=10)


class User(Model):
    age = IntegerField()
    name = CharField()

    class Meta:
        database = db

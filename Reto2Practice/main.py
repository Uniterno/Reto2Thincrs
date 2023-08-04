import datetime
from db.migrations import create_db
from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController

from schemas.account import Account
from schemas.card import Card
from schemas.user import User

if __name__ == '__main__':
    create_db('./db/db_oltp.db')

    user = UserController.create_user(age=60, name='Juan Gomez')

    account = AccountController.create_account(user=user,
                                               balance=0,
                                               open_date=datetime.datetime.now(),
                                               limit=50000)
    card = CardController.create_card(account=account, user=user, cvv='123')

    for i in Account.select():
        print(i.id, i.user_id, i.balance, i.open_date, i.limit)

    for i in User.select():
        print(i.id, i.age, i.name)

    for i in Card.select():
        print(i.id, i.account_id, i.name, i.cvv)

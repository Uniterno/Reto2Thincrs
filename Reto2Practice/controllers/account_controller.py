from schemas.account import Account, User
from schemas.card import Card
from typing import Union

import datetime


# from typing

class AccountController:
    # Create account
    @staticmethod
    def create_account(
            user: User,
            balance: float,
            open_date: datetime.datetime,
            limit: float):
        account = Account(user_id=user.id, balance=balance, open_date=open_date, limit=limit)
        account.save()
        return account

    # Read
    @staticmethod
    def get_account_by_id(id: int) -> Account:
        return Account.get(id=id)

    @staticmethod
    def get_account_by_user(user: User) -> Union[Account, None]:
        try:
            return Account.get(user_id=user.id)
        except Account.DoesNotExist:
            return None

    @staticmethod
    def get_account_by_card(card: Card) -> Account:
        return Card.get(id=card.account_id)

    # Update 
    @staticmethod
    def update_balance(account, amount) -> bool:
        balance = account.balance + amount
        limit = account.limit
        # if balance <= limit:
        if balance > -limit:
            account.balance = balance
            account.save()
            return True
        else:
            print('Not enough credit')
            return False

    @staticmethod
    def update_limit(account: Account, limit: int):
        if limit > 0:
            account.limit = limit
            account.save()
        else:
            print("Limit must be positive")

    # Delete
    @staticmethod
    def delete_account(account: Account):
        try:
            card = Account.get(account_id=account.id)
        except FileNotFoundError:
            card = None
        if card is None:
            account.delete_instance()
        else:
            card.delete_instance()
            account.delete_instance()

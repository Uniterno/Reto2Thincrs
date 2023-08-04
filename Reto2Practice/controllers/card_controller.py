from schemas.account import Account, User
from schemas.card import Card
from typing import Union


class CardController:

    # Create
    @staticmethod
    def create_card(account: Account, user: User, cvv: str) -> Card:
        card = Card(account_id=account.id, name=user.name, cvv=cvv)
        card.save()
        return card

    # Read
    @staticmethod
    def get_card_by_id(id: int) -> Union[Card, None]:
        try:
            return Card.get(id=id)
        except Card.DoesNotExist:
            return None

    @staticmethod
    def get_card_by_account(account: Account) -> Union[Card, None]:
        try:
            return Card.filter(account_id=account.id)
        except Card.DoesNotExist:
            return None

    # Delete
    @staticmethod
    def delete_card(card: Card):
        account = Account.get(id=card.account_id)
        balance = account.balance
        if balance == 0:
            card.delete_instance()
        else:
            print('Balance must be zero to delete this card')

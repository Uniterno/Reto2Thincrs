import datetime
from typing import Union, List

from schemas.account import Account
from schemas.payment import Payment

from controllers.account_controller import AccountController


class PaymentController:
    # create
    @staticmethod
    def make_payment(account: Account, date_time: datetime.datetime, amount: float):

        amount = -amount

        if AccountController.update_balance(account=account, amount=amount) & (amount < 0):
            account_id = account.id
            payment = Payment(account_id=account_id, date_time=date_time, amount=amount)
            payment.save()
            print(f"Payment successfully made for account: {account_id}")
            return payment
        else:
            print("Payment failed")

    # read
    @staticmethod
    def get_payment_by_id(id: int) -> Union[Payment, None]:
        try:
            return Payment.get(id=id)
        except Account.DoesNotExist:
            print(f"Payment with id {id} does not exist")
            return None

    @staticmethod
    def get_payments_by_account(account: Account) -> Union[List, None]:
        try:
            return list(Payment.filter(account_id=account.id))
        except Payment.DoesNotExist:
            print(f"No payments were found in account with id {id}")
            return None

    # delete
    @staticmethod
    def delete_payment(payment: Payment):
        payment.delete_instance()

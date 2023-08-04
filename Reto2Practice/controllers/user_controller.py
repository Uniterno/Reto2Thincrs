from controllers.account_controller import AccountController
from schemas.user import User
from schemas.account import Account


class UserController:

    # Create
    @staticmethod
    def create_user(age: int, name: str) -> User:
        user = User(age=age, name=name)
        user.save()
        return user

    # Read
    @staticmethod
    def get_user_by_id(id: int) -> User:
        return User.get(id=id)

    @staticmethod
    def get_user_by_name(name: str) -> User:
        return User.get(name=name)

    # Update
    @staticmethod
    def update_name(user: User, name: str) -> User:
        user.name = name
        user.save()
        return user

    # Delete
    @staticmethod
    def delete_user(user: User):
        try:
            account = Account.get(user_id=user.id)
        except FileNotFoundError:
            account = None
        if account is None:
            user.delete_instance()
        else:
            AccountController.delete_account(account=account)
            user.delete_instance()

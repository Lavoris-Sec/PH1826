class InsufficientFundsError(Exception):
    pass
    # def __init__(self, message, error_code):
    #     super().__init__(message)
    #     self.error_code = error_code


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Недостаточно средств.")

    new_balance = balance - amount
    print(f"Операция успешна! Снято: {amount}. Оставшийся баланс: {new_balance}")
    return new_balance


try:
    withdraw(balance=10000, amount=15000)
except InsufficientFundsError as e:
    print(f"Ошибка: {e}")

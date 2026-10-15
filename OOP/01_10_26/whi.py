# class MyError(Exception):
#     """Леша вами не доволен"""
#     pass
#
#
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("##################\nубери ноль этот\n##################\n")
#
# try:
#     raise MyError("ойе")
# except MyError as e:
#     print(f'Недовольство: {e}')


class ValidationError(Exception):
    def __init__(self, message, error_code, user_id=None):
        super().__init__(message)
        self.error_code = error_code
        self.user_id = user_id


def check_age(age, user_id):
    if age < 18:
        raise ValidationError(
            message="Пользователь слишком молод",
            error_code=403,
            user_id=user_id
        )


try:
    check_age(15, user_id="user_123")
except ValidationError as e:
    print(f"Ошибка {e.error_code}: {e} Пользователь: {e.user_id})")

class AppValidationError(Exception):
    def __init__(self, message, field, status_code):
        super().__init__(message)
        self.field = field
        self.status_code = status_code


def register_user(username, email):
    if '@' not in email:
        raise AppValidationError(
            message=f"{username} передал неверный формат",
            field=email,
            status_code=400
        )


try:
    register_user("aboba", "fghjk.com")
except AppValidationError as e:
    print(f"Ошибка {e.status_code} в поле {e.field} #{e}")

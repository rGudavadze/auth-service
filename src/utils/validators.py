from utils.exceptions import PasswordMismatchException


class PasswordMatchValidator:
    def __call__(self, attrs, **kwargs):
        """
        Validation checks that password and password_confirm have the same value.
        """

        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")

        if password != password_confirm:
            raise PasswordMismatchException()

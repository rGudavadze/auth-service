from rest_framework import status
from rest_framework.exceptions import APIException


class PasswordMismatchException(APIException):
    """
    raise if password and password_confirm mismatch.
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Password and Password Confirm fields must have the same value."
    default_code = "bad_request"


class InvalidEmailOrPasswordException(APIException):
    """
    raise if email or password is invalid.
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Invalid email or password."
    default_code = "bad_request"


class InvalidTokenTypeException(APIException):
    """
    raise if token type is wrong invalid.
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Invalid token type."
    default_code = "bad_request"

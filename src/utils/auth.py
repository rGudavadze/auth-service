from datetime import datetime, timedelta
from uuid import UUID, uuid4

import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

from apps.staff.models import Employee
from apps.users.models import User


class TokenVerification:
    @classmethod
    def create_token(cls, user_id: UUID, exp_time: int, token_type: str):
        header = {"typ": settings.JWT_TOKEN_TYP}

        user_info = cls.generate_user_information(user_id=user_id)

        payload = {
            "sub": user_info,
            "exp": datetime.utcnow() + timedelta(minutes=exp_time),
            "jti": uuid4().hex,
            "user_id": user_id,
            "iat": datetime.utcnow(),
            "token_type": token_type,
        }

        token = jwt.encode(
            headers=header,
            payload=payload,
            key=settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM,
        )

        return token

    @classmethod
    def create_access_token(cls, user_id: UUID):
        access_token = cls.create_token(
            user_id=user_id,
            exp_time=settings.JWT_TOKEN_EXP_TIME,
            token_type="access",
        )
        return access_token

    @classmethod
    def create_refresh_token(cls, user_id: UUID):
        refresh_token = cls.create_token(
            user_id=user_id,
            exp_time=settings.JWT_REFRESH_TOKEN_EXP_TIME,
            token_type="refresh",
        )
        return refresh_token

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(
                jwt=token, key=settings.JWT_SECRET_KEY, algorithms=settings.JWT_ALGORITHM
            )

            return payload

        except jwt.DecodeError:
            raise AuthenticationFailed("Token is invalid.")

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired.")

    @staticmethod
    def generate_user_information(user_id):
        user_info = dict()
        user = User.objects.filter(pk=user_id).first()

        user_info["user"] = user_id

        if hasattr(user, "customer"):
            user_info["customer"] = str(user.customer.id)

        elif hasattr(user, "employee"):
            employee = (
                Employee.objects.select_related("department").filter(user=user_id).first()
            )
            user_info.update(
                {
                    "employee": str(user.employee.id),
                    "department": {
                        "id": str(employee.department.id),
                        "name": employee.department.name,
                    },
                }
            )

        return user_info

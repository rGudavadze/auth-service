from datetime import datetime, timedelta
from uuid import UUID

import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed


class TokenVerification:
    @staticmethod
    def create_token(user_id: UUID, exp_time: int, token_type: str):
        header = {"typ": settings.JWT_TOKEN_TYP}

        payload = {
            "sub": user_id,
            "exp": datetime.utcnow() + timedelta(minutes=exp_time),
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

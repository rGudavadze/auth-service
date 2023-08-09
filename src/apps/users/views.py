from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers import (
    LoginSerializer,
    RefreshTokenSerializer,
    RegisterSerializer,
)
from utils.auth import TokenVerification


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):  # noqa
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.data.get("user_id")

        access_token = TokenVerification.create_access_token(user_id=user_id)
        refresh_token = TokenVerification.create_refresh_token(user_id=user_id)

        response_data = dict(access_token=access_token, refresh_token=refresh_token)

        return Response(response_data)


class RefreshTokenAPIView(APIView):
    serializer_class = RefreshTokenSerializer

    def post(self, request, *args, **kwargs):  # noqa
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        payload = serializer.data.get("payload")

        access_token = TokenVerification.create_access_token(user_id=payload.get("sub"))

        return Response(data={"access_token": access_token})

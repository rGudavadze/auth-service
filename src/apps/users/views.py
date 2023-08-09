from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers import LoginSerializer
from utils.auth import TokenVerification


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

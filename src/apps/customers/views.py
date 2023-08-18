from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.customers.models import Customer
from apps.customers.serializers import (
    CustomerRegisterSerializer,
    CustomerSerializer,
)
from utils.logger import logger


class CustomerRegisterAPIView(APIView):
    serializer_class = CustomerRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        logger(f"Customer with id: {serializer.data.get('id')} has been registered.")

        return Response(
            {"detail": "you have successfully created your account."},
            status=status.HTTP_201_CREATED,
        )


class CustomerListAPIView(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerDetailsAPIView(RetrieveAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

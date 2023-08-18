from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.staff.models import Department, Employee
from apps.staff.serializers import (
    DepartmentSerializer,
    EmployeeRegisterSerializer,
    EmployeeSerializer,
)
from utils.logger import logger


class DepartmentListAPIView(ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentDetailAPIView(RetrieveAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class EmployeeRegisterAPIView(APIView):
    serializer_class = EmployeeRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        logger(f"Employee with id: {serializer.data.get('id')} has been registered.")

        return Response(
            {"detail": "you have successfully created your account."},
            status=status.HTTP_201_CREATED,
        )


class EmployeeListAPIView(ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDetailsAPIView(RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

from rest_framework import generics
from .serializers import *


class ListCreateEmployee(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyEmployee(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ListCreatePolicies(generics.ListCreateAPIView):
    queryset = Policies.objects.all()
    serializer_class = PoliciesSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyPolicies(generics.RetrieveDestroyAPIView):
    queryset = Policies.objects.all()
    serializer_class = PoliciesSerializer


class ListCreateProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyProduct(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from rest_framework import generics
from .serializers import *


class ListCreateCustomer(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyGeneralLedgerAccounts(generics.RetrieveDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

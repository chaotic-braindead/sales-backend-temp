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


class ListCreateChartOfAccounts(generics.ListCreateAPIView):
    queryset = ChartOfAccounts.objects.all()
    serializer_class = ChartOfAccountsSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyChartOfAccounts(generics.RetrieveDestroyAPIView):
    queryset = ChartOfAccounts.objects.all()
    serializer_class = ChartOfAccountsSerializer


class ListCreateGeneralLedgerAccounts(generics.ListCreateAPIView):
    queryset = GeneralLedgerAccounts.objects.all()
    serializer_class = GeneralLedgerAccountsSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyGeneralLedgerAccounts(generics.RetrieveDestroyAPIView):
    queryset = GeneralLedgerAccounts.objects.all()
    serializer_class = GeneralLedgerAccountsSerializer


class ListCreateBusinessPartnerMaster(generics.ListCreateAPIView):
    queryset = BusinessPartnerMaster.objects.all()
    serializer_class = BusinessPartnerMasterSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyBusinessPartnerMaster(generics.RetrieveDestroyAPIView):
    queryset = BusinessPartnerMaster.objects.all()
    serializer_class = BusinessPartnerMasterSerializer

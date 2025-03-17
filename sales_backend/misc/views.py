from rest_framework import viewsets
from .serializers import *


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class PoliciesViewSet(viewsets.ModelViewSet):
    queryset = Policies.objects.all()
    serializer_class = PoliciesSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ChartOfAccountsViewSet(viewsets.ModelViewSet):
    queryset = ChartOfAccounts.objects.all()
    serializer_class = ChartOfAccountsSerializer


class GeneralLedgerAccountsViewSet(viewsets.ModelViewSet):
    queryset = GeneralLedgerAccounts.objects.all()
    serializer_class = GeneralLedgerAccountsSerializer


class BusinessPartnerMasterViewSet(viewsets.ModelViewSet):
    queryset = BusinessPartnerMaster.objects.all()
    serializer_class = BusinessPartnerMasterSerializer


class ReworkOrderViewSet(viewsets.ModelViewSet):
    queryset = ReworkOrder.objects.all()
    serializer_class = ReworkOrderSerializer


class GoodsIssueViewSet(viewsets.ModelViewSet):
    queryset = GoodsIssue.objects.all()
    serializer_class = GoodsIssueSerializer

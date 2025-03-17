from rest_framework import generics
from .models import *
from .serializers import QuotationSerializer, QuotationItemsSerializer


class ListCreateQuotation(generics.ListCreateAPIView):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyUpdateQuotation(generics.RetrieveDestroyAPIView):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer


class ListCreateQuotationItems(generics.ListCreateAPIView):
    queryset = QuotationItems.objects.all()
    serializer_class = QuotationItemsSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyUpdateQuotationItems(generics.RetrieveDestroyAPIView):
    queryset = QuotationItems.objects.all()
    serializer_class = QuotationItemsSerializer

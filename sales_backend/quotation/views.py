from rest_framework import generics
from .models import *
from .serializers import QuotationSerializer, QuotationItemsSerializer
from rest_framework.response import Response
from rest_framework import status


class ListCreateQuotation(generics.ListCreateAPIView):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer
    model = serializer_class.Meta.model


class RetrieveUpdateDestroyQuotation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer


# class ListCreateQuotationItems(generics.ListAPIView):
#     serializer_class = QuotationItemsSerializer
#     model = serializer_class.Meta.model

#     def get_queryset(self):
#         quotation_id = self.kwargs["quotation_id"]
#         return QuotationItems.objects.filter(pk=quotation_id)


# class RetrieveDestroyQuotationItems(generics.RetrieveDestroyAPIView):
#     serializer_class = QuotationItemsSerializer

#     def get_object(self):
#         quotation_id = self.kwargs["quotation_id"]
#         qitems_id = self.kwargs["qitems_id"]

#         try:
#             return QuotationItems.objects.get(
#                 quotation_id=quotation_id, qitems_id=qitems_id
#             )
#         except QuotationItems.DoesNotExist:
#             return Response(
#                 {"error": "Quotation Item not found."}, status=status.HTTP_404_NOT_FOUND
#             )

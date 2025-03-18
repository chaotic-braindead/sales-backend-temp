from rest_framework import viewsets
from .serializers import *
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from quotation.models import Quotation, QuotationItems
from rest_framework import status


class BlanketAgreementViewSet(viewsets.ModelViewSet):
    queryset = BlanketAgreement.objects.all()
    serializer_class = BlanketAgreementSerializer

    def create(self, request: Request, *args, **kwargs):
        # convert quotation_id to sales order
        quotation_id = request.data.pop("quotation_id")
        quotation = get_object_or_404(Quotation, pk=quotation_id)

        body = request.data

        quotation_items: list[QuotationItems] = get_list_or_404(
            QuotationItems, quotation_id=quotation
        )
        to_create = []

        agreement = BlanketAgreement.objects.create(
            customer_id=quotation.customer_id,
            salesrep_id=quotation.salesrep_id,
            total_value=quotation.total_amount,
            **body
        )

        for item in quotation_items:
            data = {
                "agreement_id": agreement,
                "product_id": item.product_id,
                "agreed_quantity": item.quantity,
                "unit_price": item.unit_price,
            }
            to_create.append(BlanketAgreementItems(**data))
        BlanketAgreementItems.objects.bulk_create(to_create)
        return Response(
            BlanketAgreementSerializer(agreement).data, status=status.HTTP_201_CREATED
        )

from rest_framework import viewsets
from .serializers import *
from rest_framework.request import Request
from quotation.serializers import QuotationItems, Quotation
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework import status


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def create(self, request: Request, *args, **kwargs):
        # convert quotation_id to sales order
        quotation_id = request.data.get("quotation_id")
        quotation = get_object_or_404(Quotation, pk=quotation_id)
        order_date = request.data.get("order_date", quotation.date_issued)
        order_type = request.data.get("order_type")
        markup = request.data.get("markup")
        quotation_items: list[QuotationItems] = get_list_or_404(
            QuotationItems, quotation_id=quotation
        )
        to_create = []

        order = Orders.objects.create(
            customer_id=quotation.customer_id,
            salesrep_id=quotation.salesrep_id,
            quotation_id=quotation,
            order_date=order_date,
            order_type=order_type,
            order_total_amount=quotation.total_amount,
        )

        # if quotation is Non-Project Based, send to MRP for pricing
        if quotation.type == Quotation.Type.NON_PROJECT_BASED:
            pass
        # else, obtain bill of materials
        else:
            pass

        for item in quotation_items:
            data = {
                "order_id": order,
                "item_id": item.product_id,
                "quantity": item.quantity,
                "unit_price": item.unit_price,
                "discount": 0,
                "total_price": item.total_price,
                "markup_percentage": markup,
            }
            to_create.append(OrderItems(**data))
        OrderItems.objects.bulk_create(to_create)
        return Response(OrdersSerializer(order).data, status=status.HTTP_201_CREATED)

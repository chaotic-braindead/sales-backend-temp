from rest_framework import serializers
from .models import *
from invoice.serializers import SalesInvoicesSerializer


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    items = OrderItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Orders
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        invoice = instance.invoice.first()
        data["invoice"] = SalesInvoicesSerializer(invoice).data if invoice else None
        return data

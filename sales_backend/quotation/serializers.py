from rest_framework import serializers
from .models import *
from misc.serializers import ProductSerializer, EmployeeSerializer
from customer.serializers import CustomerSerializer
from decimal import Decimal


class QuotationItemsSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()

    class Meta:
        model = QuotationItems
        fields = "__all__"
        read_only_fields = ["quotation_id", "qitems_id"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["product"] = data.pop("product_id")
        return data


class QuotationSerializer(serializers.ModelSerializer):
    items = QuotationItemsSerializer(many=True)
    customer_id = CustomerSerializer()
    salesrep_id = EmployeeSerializer()

    class Meta:
        model = Quotation
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["customer"] = data.pop("customer_id")
        data["salesrep"] = data.pop("salesrep_id")
        return data

    def create(self, validated_data):
        items_data = validated_data.pop("items")

        quotation = Quotation.objects.create(**validated_data)
        quotation_items = []
        total_amount = Decimal(0)
        for item in items_data:
            data = {**item, "quotation_id": quotation}
            quotation_items.append(QuotationItems(**data))
            total_amount += item["quantity"] * item["unit_price"]

        QuotationItems.objects.bulk_create(quotation_items)

        quotation.total_amount = total_amount
        quotation.save()
        return quotation

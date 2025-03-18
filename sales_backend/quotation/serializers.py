from rest_framework import serializers
from .models import *
from decimal import Decimal
from misc.serializers import ProductSerializer, Product, EmployeeSerializer
from customer.serializers import CustomerSerializer


class QuotationItemsSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = QuotationItems
        exclude = ["product_id"]
        read_only_fields = ["quotation_id", "qitems_id"]

    def get_product(self, obj):
        return ProductSerializer(obj.product_id).data


class QuotationSerializer(serializers.ModelSerializer):
    items = QuotationItemsSerializer(many=True)
    customer = serializers.SerializerMethodField()
    salesrep = serializers.SerializerMethodField()

    class Meta:
        model = Quotation
        exclude = ["customer_id", "salesrep_id"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")

        quotation = Quotation.objects.create(**validated_data)
        quotation_items = []
        total_amount = Decimal(0)
        for item in items_data:
            item["quotation_id"] = quotation
            item["total_price"] = item["quantity"] * item["unit_price"]
            quotation_items.append(QuotationItems(**item))
            total_amount += item["quantity"] * item["unit_price"]

        QuotationItems.objects.bulk_create(quotation_items)

        quotation.total_amount = total_amount
        quotation.save()
        return quotation

    def get_customer(self, obj):
        return CustomerSerializer(obj.customer_id).data

    def get_salesrep(self, obj):
        return EmployeeSerializer(obj.salesrep_id).data

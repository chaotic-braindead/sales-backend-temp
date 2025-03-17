from rest_framework import serializers
from .models import *
from misc.serializers import ProductSerializer, Product
from customer.serializers import Customer, CustomerSerializer
from decimal import Decimal


class QuotationItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationItems
        fields = "__all__"
        read_only_fields = ["quotation_id", "qitems_id"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        product_id = data.pop("product_id")
        product_data = ProductSerializer(Product.objects.get(pk=product_id)).data
        data = {**data, **product_data}
        return data


class QuotationSerializer(serializers.ModelSerializer):
    items = QuotationItemsSerializer(many=True)

    class Meta:
        model = Quotation
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        customer_id = data.pop("customer_id")
        customer = Customer.objects.get(customer_id=customer_id)
        data["customer"] = CustomerSerializer(customer).data
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

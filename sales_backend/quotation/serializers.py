from rest_framework import serializers
from .models import *
from decimal import Decimal
from misc.serializers import ProductSerializer, Product


class QuotationItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationItems
        fields = "__all__"
        read_only_fields = ["quotation_id", "qitems_id"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        product_id = data.pop("product_id")
        data["product"] = ProductSerializer(Product.objects.get(pk=product_id)).data
        return data


class QuotationSerializer(serializers.ModelSerializer):
    items = QuotationItemsSerializer(many=True)

    class Meta:
        model = Quotation
        fields = "__all__"

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

from rest_framework import serializers
from .models import *


class QuotationItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationItems
        fields = "__all__"


class QuotationSerializer(serializers.ModelSerializer):
    items = QuotationItemsSerializer(many=True)

    class Meta:
        model = Quotation
        fields = "__all__"

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        quotation = Quotation.objects.create(**validated_data)

        quotation_items = []
        total_amount = 0.0
        for item in items_data:
            quotation_items.append(QuotationItems(quotation_id=quotation, **item))
            total_amount += item["quantity"] * item["unit_price"]

        QuotationItems.objects.bulk_create(quotation_items)

        quotation.total_amount = total_amount
        quotation.save()

from rest_framework import serializers
from .models import *
from decimal import Decimal


class BlanketAgreementItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlanketAgreementItems
        fields = "__all__"


class BlanketAgreementSerializer(serializers.ModelSerializer):
    items = BlanketAgreementItemsSerializer(many=True)

    class Meta:
        model = BlanketAgreement
        fields = "__all__"

    def create(self, validated_data):
        items_data = validated_data.pop("items")

        agreement = BlanketAgreement.objects.create(**validated_data)
        agreement_items = []
        total_amount = Decimal(0)
        for item in items_data:
            data = {**item, "agreement_id": agreement}
            agreement_items.append(BlanketAgreementItems(**data))
            total_amount += item["quantity"] * item["unit_price"]

        BlanketAgreementItems.objects.bulk_create(agreement_items)

        agreement.total_value = total_amount
        agreement.save()
        return agreement

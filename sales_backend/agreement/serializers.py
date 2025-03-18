from rest_framework import serializers
from .models import *
from misc.serializers import ProductSerializer


class BlanketAgreementItemsSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()

    class Meta:
        model = BlanketAgreementItems
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["product"] = data.pop("product_id")
        return data


class BlanketAgreementSerializer(serializers.ModelSerializer):
    items = BlanketAgreementItemsSerializer(many=True)

    class Meta:
        model = BlanketAgreement
        fields = "__all__"

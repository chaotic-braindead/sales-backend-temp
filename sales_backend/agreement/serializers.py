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

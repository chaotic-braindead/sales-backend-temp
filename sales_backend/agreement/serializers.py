from rest_framework import serializers
from .models import *
from misc.serializers import ProductSerializer


class BlanketAgreementItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlanketAgreementItems
        fields = "__all__"


class BlanketAgreementSerializer(serializers.ModelSerializer):
    items = BlanketAgreementItemsSerializer(many=True)

    class Meta:
        model = BlanketAgreement
        fields = "__all__"

from rest_framework import serializers
from .models import *
from misc.serializers import NonProjectOrderPricingSerializer, BOMSerializer


class SalesCostingSerializer(serializers.ModelSerializer):
    non_project_costing_id = NonProjectOrderPricingSerializer()
    bom_id = BOMSerializer()

    class Meta:
        model = SalesCosting
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["non_project_costing"] = data.pop("non_project_costing_id")
        data["bom"] = data.pop("bom_id")
        return data

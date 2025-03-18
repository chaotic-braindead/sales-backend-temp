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
        np_costing = data.pop("non_project_costing_id")
        data["non_project_costing"] = np_costing
        bom = data.pop("bom_id")
        data["bom"] = bom
        return data

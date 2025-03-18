from rest_framework import serializers
from .models import *
from misc.serializers import (
    ProductSerializer,
    GoodsIssueSerializer,
    ReworkOrderSerializer,
    EmployeeSerializer,
)
from costing.serializers import SalesCostingSerializer
from customer.serializers import CustomerSerializer
from invoice.serializers import SalesInvoicesSerializer


class OrderItemsSerializer(serializers.ModelSerializer):
    item_id = ProductSerializer()
    sales_costing_id = SalesCostingSerializer()

    class Meta:
        model = OrderItems
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        item = data.pop("item_id")
        sales_costing = data.pop("sales_costing_id")
        data["item"] = item
        data["sales_costing"] = sales_costing
        return data


class OrdersSerializer(serializers.ModelSerializer):
    customer_id = CustomerSerializer()
    salesrep_id = EmployeeSerializer()
    items = OrderItemsSerializer(many=True)
    goods_issue_id = GoodsIssueSerializer()
    rework_id = ReworkOrderSerializer()

    class Meta:
        model = Orders
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        goods_issue = data.pop("goods_issue_id")
        data["goods_issue"] = goods_issue
        rework = data.pop("rework_id")
        data["rework"] = rework
        customer = data.pop("customer_id")
        data["customer"] = customer
        salesrep = data.pop("salesrep_id")
        data["salesrep"] = salesrep

        invoice = instance.invoice.first()
        data["invoice"] = SalesInvoicesSerializer(invoice).data if invoice else None
        return data

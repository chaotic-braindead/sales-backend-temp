from rest_framework import serializers
from .models import *
from invoice.serializers import SalesInvoicesSerializer
from misc.serializers import (
    ProductSerializer,
    EmployeeSerializer,
    ReworkOrderSerializer,
    GoodsIssueSerializer,
)
from costing.serializers import SalesCostingSerializer
from customer.serializers import CustomerSerializer
from agreement.serializers import BlanketAgreementSerializer


class OrderItemsSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    sales_costing = serializers.SerializerMethodField()

    class Meta:
        model = OrderItems
        exclude = ["item_id", "sales_costing_id"]

    def get_item(self, obj):
        return ProductSerializer(obj.item_id).data

    def get_sales_costing(self, obj):
        return SalesCostingSerializer(obj.sales_costing_id).data


class OrdersSerializer(serializers.ModelSerializer):
    items = OrderItemsSerializer(many=True, read_only=True)
    customer = serializers.SerializerMethodField()
    salesrep = serializers.SerializerMethodField()
    agreement = serializers.SerializerMethodField()
    rework = serializers.SerializerMethodField()
    goods_issue = serializers.SerializerMethodField()

    class Meta:
        model = Orders
        exclude = [
            "customer_id",
            "salesrep_id",
            "agreement_id",
            "rework_id",
            "goods_issue_id",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        invoice = instance.invoice.first()
        data["invoice"] = SalesInvoicesSerializer(invoice).data if invoice else None
        return data

    def get_customer(self, obj):
        return CustomerSerializer(obj.customer_id).data

    def get_salesrep(self, obj):
        return EmployeeSerializer(obj.salesrep_id).data

    def get_agreement(self, obj):
        return (
            BlanketAgreementSerializer(obj.agreement_id).data
            if obj.agreement_id
            else None
        )

    def get_rework(self, obj):
        return ReworkOrderSerializer(obj.rework_id).data if obj.rework_id else None

    def get_goods_issue(self, obj):
        return (
            GoodsIssueSerializer(obj.goods_issue_id).data
            if obj.goods_issue_id
            else None
        )

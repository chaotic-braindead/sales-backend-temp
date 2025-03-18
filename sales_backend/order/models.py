from django.db import models
from datetime import datetime


class Orders(models.Model):
    class Status(models.TextChoices):
        PENDING = "Pending"
        PROCESSED = "Processed"
        SHIPPED = "Shipped"
        DELIVERED = "Delivered"
        CANCELLED = "Cancelled"

    class Type(models.TextChoices):
        DIRECT = "Direct"
        SCHEDULED = "Scheduled"
        OPEN = "Open"
        D3_SAMPLE = "D3 Sample"

    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(to="customer.Customer", on_delete=models.CASCADE)
    salesrep_id = models.ForeignKey(
        to="misc.Employee", on_delete=models.SET_NULL, null=True
    )
    quotation_id = models.ForeignKey(
        to="quotation.Quotation", on_delete=models.SET_NULL, blank=True, null=True
    )
    agreement_id = models.ForeignKey(
        to="agreement.BlanketAgreement",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    # used to see if order needs a rework
    rework_id = models.ForeignKey(
        to="misc.ReworkOrder", on_delete=models.SET_NULL, blank=True, null=True
    )
    goods_issue_id = models.ForeignKey(
        to="misc.GoodsIssue", on_delete=models.SET_NULL, blank=True, null=True
    )
    order_date = models.DateTimeField(default=datetime.now())
    order_status = models.TextField(choices=Status, default="Pending")
    order_total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_type = models.TextField(choices=Type)

    def send_non_project_to_MRP(self):
        pass


class OrderItems(models.Model):
    class DemandLevel(models.TextChoices):
        LOW = "Low Demand"
        MEDIUM = "Medium Demand"
        HIGH = "High Demand"
        VERY_HIGH = "Very High Demand"
        SEASONAL = "Seasonal Demand"

    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(
        to=Orders, on_delete=models.CASCADE, related_name="items"
    )
    item_id = models.ForeignKey(to="misc.Product", on_delete=models.SET_NULL, null=True)
    sales_costing_id = models.ForeignKey(
        to="costing.SalesCosting", on_delete=models.SET_NULL, null=True
    )
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    demand_level = models.TextField(choices=DemandLevel, default=DemandLevel.LOW)

    # adds a markup to the price from sales_costing. unit_price must adjust accordingly
    markup_percentage = models.DecimalField(max_digits=10, decimal_places=2)

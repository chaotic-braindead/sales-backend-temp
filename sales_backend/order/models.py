from django.db import models


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
    rework_id = models.ForeignKey(to="misc.ReworkOrder", on_delete=models.CASCADE)
    goods_issue_id = models.ForeignKey(to="misc.GoodsIssue", on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    order_status = models.TextField(choices=Status)
    order_type = models.TextField(choices=Type)


class OrderItems(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(to=Orders, on_delete=models.CASCADE)
    item_id = models.ForeignKey(to="misc.Product", on_delete=models.SET_NULL, null=True)
    sales_costing_id = models

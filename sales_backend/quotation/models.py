from django.db import models
from datetime import datetime


class Quotation(models.Model):
    class Type(models.TextChoices):
        PROJECT_BASED = "Project Based"
        NON_PROJECT_BASED = "Non-Project Based"
        SERVICE = "Service"

    class Status(models.TextChoices):
        PENDING = "Pending"
        APPROVED = "Approved"
        REJECTED = "Rejected"

    quotation_id = models.BigAutoField(primary_key=True)
    customer_id = models.ForeignKey(
        to="customer.Customer", on_delete=models.SET_NULL, null=True
    )
    salesrep_id = models.ForeignKey(
        to="misc.Employee", on_delete=models.SET_NULL, null=True
    )
    date_issued = models.DateTimeField(default=datetime.now())
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type = models.TextField(choices=Type)
    status = models.TextField(choices=Status, default=Status.PENDING)


class QuotationItems(models.Model):
    qitems_id = models.BigAutoField(primary_key=True)
    quotation_id = models.ForeignKey(
        to=Quotation, on_delete=models.CASCADE, related_name="items"
    )
    product_id = models.ForeignKey(
        to="misc.Product", on_delete=models.SET_NULL, null=True
    )
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

from django.db import models
from datetime import datetime


class BlanketAgreement(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "Active"
        EXPIRED = "Expired"
        CANCELLED = "Cancelled"

    class AgreementMethod(models.TextChoices):
        WRITTEN = "Written"
        ORAL = "Oral"
        ELECTRONIC = "Electronic"

    agreement_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(to="customer.Customer", on_delete=models.CASCADE)
    salesrep_id = models.ForeignKey(to="misc.Employee", on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now())
    end_date = models.DateTimeField(default=datetime.now())
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.TextField(choices=Status)
    description = models.CharField(max_length=255)
    signed_date = models.DateTimeField(default=datetime.now())
    agreement_method = models.TextField(choices=AgreementMethod)


class BlanketAgreementItems(models.Model):
    agreement_items_id = models.AutoField(primary_key=True)
    agreement_id = models.ForeignKey(
        to=BlanketAgreement, on_delete=models.CASCADE, related_name="items"
    )
    product_id = models.ForeignKey(to="misc.Product", on_delete=models.CASCADE)
    agreed_quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import models


class Quotation(models.Model):
    class Type(models.TextChoices):
        PROJECT_BASED = "Project Based"
        NON_PROJECT_BASED = "Non Project Based"
        SERVICE = "Service"

    class Status(models.TextChoices):
        PENDING = "Pending"
        APPROVED = "Approved"
        REJECTED = "Rejected"

    quotation_id = models.BigAutoField(primary_key=True)
    customer_id = models.ForeignKey(to="customer.Customer", on_delete=models.SET_NULL)
    salesresp_id = models.ForeignKey(to="misc.Employee", on_delete=models.SET_NULL)
    date_issued = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(decimal_places=2, default=0)
    type = models.TextField(choices=Type)
    status = models.TextField(choices=Status)


class QuotationItems(models.Model):
    qitems_id = models.BigAutoField(primary_key=True)
    quotation_id = models.ForeignKey(to=Quotation, on_delete=models.CASCADE)
    product_id = models.ForeignKey(to="misc.Product", on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2)
    total_price = models.DecimalField(decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

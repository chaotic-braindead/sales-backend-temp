from django.db import models


class Employee(models.Model):
    employee_id = models.BigAutoField(primary_key=True)
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    phone = models.TextField(max_length=255)
    job_title = models.TextField(max_length=255)


class Policies(models.Model):
    policy_id = models.BigAutoField(primary_key=True)
    policy_name = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    effective_date = models.DateField(auto_now_add=True)


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    unit_of_measure = models.TextField(max_length=255, default="kg")
    policy_id = models.ForeignKey(to=Policies, on_delete=models.CASCADE)

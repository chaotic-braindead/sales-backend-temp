from rest_framework import serializers
from .models import *


class SalesInvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoices
        fields = "__all__"

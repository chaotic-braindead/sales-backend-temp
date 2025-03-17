from rest_framework import viewsets
from .models import *
from .serializers import QuotationSerializer


class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

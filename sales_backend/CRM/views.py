from rest_framework import viewsets
from .serializers import *


class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer


class CampaignsViewSet(viewsets.ModelViewSet):
    queryset = Campaigns.objects.all()
    serializer_class = CampaignsSerializer


class CampaignContactsViewSet(viewsets.ModelViewSet):
    queryset = CampaignContacts.objects.all()
    serializer_class = CampaignContactsSerializer


class OpportunitiesViewSet(viewsets.ModelViewSet):
    queryset = Opportunities.objects.all()
    serializer_class = OpportunitiesSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketConvoViewSet(viewsets.ModelViewSet):
    queryset = TicketConvo.objects.all()
    serializer_class = TicketConvoSerializer

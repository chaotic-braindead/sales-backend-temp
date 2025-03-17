from rest_framework import generics
from .serializers import *


class ListCreateLeads(generics.ListCreateAPIView):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyLeads(generics.RetrieveDestroyAPIView):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer
    model = serializer_class.Meta.model


class ListCreateCampaigns(generics.ListCreateAPIView):
    queryset = Campaigns.objects.all()
    serializer_class = CampaignsSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyCampaigns(generics.RetrieveDestroyAPIView):
    queryset = Campaigns.objects.all()
    serializer_class = CampaignsSerializer
    model = serializer_class.Meta.model


class ListCreateCampaignContacts(generics.ListCreateAPIView):
    queryset = CampaignContacts.objects.all()
    serializer_class = CampaignContactsSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyCampaignContacts(generics.RetrieveDestroyAPIView):
    queryset = CampaignContacts.objects.all()
    serializer_class = CampaignContactsSerializer
    model = serializer_class.Meta.model


class ListCreateOpportunities(generics.ListCreateAPIView):
    queryset = Opportunities.objects.all()
    serializer_class = OpportunitiesSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyOpportunities(generics.RetrieveDestroyAPIView):
    queryset = Opportunities.objects.all()
    serializer_class = OpportunitiesSerializer
    model = serializer_class.Meta.model


class ListCreateTicket(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyTicket(generics.RetrieveDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    model = serializer_class.Meta.model


class ListCreateTicketConvo(generics.ListCreateAPIView):
    queryset = TicketConvo.objects.all()
    serializer_class = TicketConvoSerializer
    model = serializer_class.Meta.model


class RetrieveDestroyTicketConvo(generics.RetrieveDestroyAPIView):
    queryset = TicketConvo.objects.all()
    serializer_class = TicketConvoSerializer
    model = serializer_class.Meta.model

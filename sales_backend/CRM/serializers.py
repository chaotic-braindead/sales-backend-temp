from rest_framework import serializers
from .models import *
from customer.serializers import CustomerSerializer

from misc.serializers import EmployeeSerializer, BusinessPartnerMasterSerializer


class LeadsSerializer(serializers.ModelSerializer):
    # campaigns = CampaignContactsSerializer(many=True)

    class Meta:
        model = Leads
        fields = "__all__"


class CampaignContactsSerializer(serializers.ModelSerializer):
    lead_id = LeadsSerializer(read_only=True)

    class Meta:
        model = CampaignContacts
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        lead = data.pop("lead_id")
        data["lead"] = lead
        return data


class CampaignsSerializer(serializers.ModelSerializer):
    contacts = CampaignContactsSerializer(many=True, read_only=True)

    class Meta:
        model = Campaigns
        fields = "__all__"


class OpportunitiesSerializer(serializers.ModelSerializer):
    customer_id = CustomerSerializer()
    salesrep_id = EmployeeSerializer()
    partner_id = BusinessPartnerMasterSerializer()

    class Meta:
        model = Opportunities
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        customer = data.pop("customer_id")
        salesrep = data.pop("salesrep_id")
        partner = data.pop("partner_id")
        data["customer"] = customer
        data["salesrep"] = salesrep
        data["partner"] = partner
        return data


class TicketConvoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketConvo
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    conversations = TicketConvoSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = "__all__"

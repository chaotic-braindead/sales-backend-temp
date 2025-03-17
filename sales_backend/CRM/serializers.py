from rest_framework import serializers
from .models import *


class CampaignContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignContacts
        fields = "__all__"


class CampaignsSerializer(serializers.ModelSerializer):
    contacts = CampaignContactsSerializer(many=True)

    class Meta:
        model = Campaigns
        fields = "__all__"

    def create(self, validated_data):
        """
        add logic on adding all campaign contacts together with
        the creation of a campaign in a single API call
        """
        contacts_data = validated_data.pop("contacts")
        campaign = Campaigns.objects.create(**validated_data)
        contacts = []
        for contact in contacts_data:
            contacts.append(CampaignContacts(**contact))

        CampaignContacts.objects.bulk_create(contacts)

        return campaign


class LeadsSerializer(serializers.ModelSerializer):
    campaigns = CampaignsSerializer(many=True)

    class Meta:
        model = Leads
        fields = "__all__"


class OpportunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunities
        fields = "__all__"


class TicketConvoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketConvo
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    conversations = TicketConvoSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = "__all__"

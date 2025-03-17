from django.urls import path
from . import views

urlpatterns = [
    path("campaigns/", views.ListCreateCampaigns.as_view()),
    path("campaigns/<int:pk>", views.RetrieveDestroyCampaigns.as_view()),
    path("leads/", views.ListCreateLeads.as_view()),
    path("leads/<int:pk>", views.RetrieveDestroyLeads.as_view()),
    path("opportunities/", views.ListCreateOpportunities.as_view()),
    path("opportunities/<int:pk>", views.RetrieveDestroyOpportunities.as_view()),
    path("ticket/", views.ListCreateTicket.as_view()),
    path("ticket/<int:pk>", views.RetrieveDestroyTicket.as_view()),
    path("ticket-convo/", views.ListCreateTicketConvo.as_view()),
    path("ticket-convo/<int:pk>", views.RetrieveDestroyTicketConvo.as_view()),
]

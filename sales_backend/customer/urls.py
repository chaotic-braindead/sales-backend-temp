from . import views
from django.urls import path

urlpatterns = [
    path("", views.ListCreateCustomer.as_view()),
    path("<int:pk>", views.RetrieveDestroyGeneralLedgerAccounts.as_view()),
]

from django.urls import path
from . import views

urlpatterns = [
    path("employee/", views.ListCreateEmployee.as_view()),
    path("employee/<int:pk>/", views.RetrieveDestroyEmployee().as_view()),
    path("policies/", views.ListCreatePolicies.as_view()),
    path("policies/<int:pk>/", views.RetrieveDestroyPolicies.as_view()),
    path("product/", views.ListCreateProduct.as_view()),
    path("product/<int:pk>/", views.RetrieveDestroyProduct.as_view()),
    path("chart-of-accounts/", views.ListCreateChartOfAccounts.as_view()),
    path("chart-of-accounts/<int:pk>/", views.RetrieveDestroyChartOfAccounts.as_view()),
    path("general-ledger-accounts/", views.ListCreateGeneralLedgerAccounts.as_view()),
    path(
        "general-ledger-accounts/<int:pk>/",
        views.RetrieveDestroyGeneralLedgerAccounts.as_view(),
    ),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListCreateQuotation.as_view()),
    path("<int:pk>/", views.RetrieveDestroyQuotation.as_view()),
    # path(
    #     "<int:quotation_id>/item/",
    #     views.ListCreateQuotationItems.as_view(),
    # ),
    # path(
    #     "<int:quotation_id>/item/<int:qitems_id>/",
    #     views.RetrieveDestroyQuotationItems.as_view(),
    # ),
]

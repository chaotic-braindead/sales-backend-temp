from django.urls import path, include
import views

urlpatterns = [
    path("", views.ListCreateQuotation.as_view()),
    path("<int:quotation_id>/", views.RetrieveDestroyQuotation.as_view()),
    # path(
    #     "<int:quotation_id>/item/",
    #     views.ListCreateQuotationItems.as_view(),
    # ),
    # path(
    #     "<int:quotation_id>/item/<int:qitems_id>/",
    #     views.RetrieveDestroyQuotationItems.as_view(),
    # ),
]

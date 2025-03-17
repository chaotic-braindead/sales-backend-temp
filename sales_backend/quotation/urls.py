from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListCreateQuotation.as_view()),
    path("<int:pk>/", views.RetrieveUpdateDestroyQuotation.as_view()),
]

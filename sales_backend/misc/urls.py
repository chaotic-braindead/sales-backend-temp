from django.urls import path
from . import views

urlpatterns = [
    path("employee/", views.ListCreateEmployee.as_view()),
    path("employee/<int:pk>/", views.RetrieveDestroyEmployee()),
    path("policies/", views.ListCreatePolicies.as_view()),
    path("policies/<int:pk>/", views.RetrieveDestroyPolicies.as_view()),
    path("product/", views.ListCreateProduct.as_view()),
    path("product/<int:pk>/", views.RetrieveDestroyProduct.as_view()),
]

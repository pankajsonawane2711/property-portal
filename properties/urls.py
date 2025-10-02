from django.urls import path
from . import views

urlpatterns = [
    path("", views.property_list, name="property_list"),
    path("add/", views.property_add, name="property_add"),
    path("mine/", views.my_properties, name="my_properties"),
    path("<slug:slug>/", views.property_detail, name="property_detail"),
    path("<slug:slug>/edit/", views.property_edit, name="property_edit"),
]

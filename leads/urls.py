from django.urls import path
from .views import create_lead
urlpatterns = [ path("create/", create_lead, name="create_lead") ]

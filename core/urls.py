from django.urls import path
from .views import home, about, contact, faq, emi

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("faq/", faq, name="faq"),
    path("emi/", emi, name="emi"),
]

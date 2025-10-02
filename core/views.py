from django.shortcuts import render
from properties.models import Property

def home(request):
    featured = Property.objects.filter(is_active=True, is_approved=True, is_featured=True)[:6]
    latest = Property.objects.filter(is_active=True, is_approved=True).order_by("-created_at")[:8]
    return render(request, "home.html", {"featured": featured, "latest": latest})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def faq(request):
    return render(request, "faq.html")

def emi(request):
    return render(request, "emi.html")

def health(request):
    from django.http import HttpResponse
    return HttpResponse("ok")

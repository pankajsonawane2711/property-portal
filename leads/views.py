from django.shortcuts import redirect
from django.contrib import messages
from .forms import LeadForm
from properties.models import Property

def create_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            p = Property.objects.get(pk=request.POST.get("property_id"))
            from .models import Lead
            lead = Lead.objects.create(
                property=p,
                name=form.cleaned_data["name"],
                phone=form.cleaned_data["phone"],
                message=form.cleaned_data.get("message",""),
                buyer=request.user if request.user.is_authenticated else None
            )
            messages.success(request, "Enquiry submitted! Builder will contact you.")
    return redirect(request.META.get("HTTP_REFERER","/"))

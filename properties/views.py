from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Property
from .forms import PropertyForm

def property_list(request):
    qs = Property.objects.filter(is_active=True, is_approved=True)
    q = request.GET.get("q")
    bhk = request.GET.get("bhk")
    loc = request.GET.get("location")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(location__icontains=q))
    if bhk:
        qs = qs.filter(bhk=bhk)
    if loc:
        qs = qs.filter(location__icontains=loc)
    return render(request, "properties/list.html", {"properties": qs})

def property_detail(request, slug):
    prop = get_object_or_404(Property, slug=slug, is_active=True, is_approved=True)
    similar = Property.objects.filter(is_active=True, is_approved=True, location=prop.location).exclude(id=prop.id)[:4]
    return render(request, "properties/detail.html", {"p": prop, "similar": similar})

@login_required
def my_properties(request):
    if not request.user.is_builder():
        return redirect("home")
    props = Property.objects.filter(builder=request.user)
    return render(request, "builder/dashboard.html", {"properties": props})

@login_required
def property_add(request):
    if not request.user.is_builder():
        return redirect("home")
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.builder = request.user
            p.is_approved = False  # moderation
            p.save()
            messages.success(request, "Property submitted. Awaiting admin approval.")
            return redirect("my_properties")
    else:
        form = PropertyForm()
    return render(request, "builder/add_property.html", {"form": form})

@login_required
def property_edit(request, slug):
    prop = get_object_or_404(Property, slug=slug, builder=request.user)
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=prop)
        if form.is_valid():
            form.save()
            messages.success(request, "Property updated.")
            return redirect("my_properties")
    else:
        form = PropertyForm(instance=prop)
    return render(request, "builder/add_property.html", {"form": form, "edit": True})

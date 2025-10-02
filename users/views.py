from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "auth/signup.html", {"form": form})

@login_required
def builder_dashboard(request):
    if not hasattr(request.user, "role") or request.user.role != "builder":
        return redirect("home")
    from properties.models import Property
    props = Property.objects.filter(builder=request.user)
    return render(request, "builder/dashboard.html", {"properties": props})

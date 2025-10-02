from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ("title","slug","price","bhk","size_sqft","location","latitude","longitude","description","is_featured","is_active")
        widgets = {
            "description": forms.Textarea(attrs={"rows":4})
        }

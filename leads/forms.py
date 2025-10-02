from django import forms
class LeadForm(forms.Form):
    name = forms.CharField(max_length=120)
    phone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea, required=False)

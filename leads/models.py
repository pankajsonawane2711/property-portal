from django.db import models
from django.conf import settings
from properties.models import Property

class Lead(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="leads")
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Lead for {self.property_id} - {self.phone}"

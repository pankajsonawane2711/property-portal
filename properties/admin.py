from django.contrib import admin
from .models import Property, Amenity

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    search_fields = ["name"]

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "bhk", "location", "is_active", "is_approved", "is_featured")
    list_filter = ("is_active", "is_approved", "is_featured", "bhk", "location")
    search_fields = ("title", "location", "description")

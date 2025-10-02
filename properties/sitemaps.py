from django.contrib.sitemaps import Sitemap
from .models import Property
class PropertySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    def items(self):
        return Property.objects.filter(is_active=True, is_approved=True)
    def location(self, obj):
        return obj.get_absolute_url()

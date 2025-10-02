from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from properties.sitemaps import PropertySitemap
from core.views import health
from core import robots as robots_mod

sitemaps = {"properties": PropertySitemap}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("users.urls")),
    path("properties/", include("properties.urls")),
    path("leads/", include("leads.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("robots.txt", robots_mod.robots_txt),
    path("health", health, name="health"),
]

from django.db import models
from django.conf import settings

class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class Property(models.Model):
    builder = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    price = models.IntegerField()
    bhk = models.IntegerField()
    size_sqft = models.IntegerField(default=0)
    location = models.CharField(max_length=120)
    latitude = models.FloatField(default=19.46)
    longitude = models.FloatField(default=72.80)
    description = models.TextField(blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=True)  # moderation gate
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("property_detail", args=[self.slug])

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("buyer", "Buyer"),
        ("builder", "Builder"),
        ("admin", "Admin"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="buyer")
    phone = models.CharField(max_length=20, blank=True)
    rera_id = models.CharField(max_length=64, blank=True)
    company = models.CharField(max_length=128, blank=True)
    is_verified_builder = models.BooleanField(default=False)

    def is_builder(self):
        return self.role == "builder"

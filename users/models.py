from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for lms."""

    USER_ROLE_CHOICES = (
        ("superadmin", "SuperAdmin"),
        ("admin", "Admin"),
        ("student", "Student"),
    )

    role = models.CharField(_("Role"), max_length=10, choices=USER_ROLE_CHOICES, default="student")

    def __str__(self):
        return self.username

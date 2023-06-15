from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db.models import (
    CharField, EmailField, BooleanField
)


# User manager class
class UserManager(BaseUserManager):
    def create_user(self, email, password, is_staff, **extra_fields):
        """Create and return an administrative or resident account
        """
        if not email or password or is_staff:
            raise ValueError("All fields must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """A helper function for the "create_user" function

            Help to create an adminstrative user account
        """
        extra_fields.setdefault("is_staff", 'admin')
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    EMPTY = None
    ADMIN = 'admin'
    RESIDENT = 'resident'

    CHOICES = [
        (EMPTY, None),
        (ADMIN, 'admin'),
        (RESIDENT, 'resident'),
    ]

    email: EmailField = models.EmailField(max_length=100, unique=True)
    is_staff: CharField = models.CharField(max_length=10, choices=CHOICES)
    is_active: BooleanField = models.BooleanField(default=True)

    class Meta:
        ordering = [
            '-email',
        ]
        indexes = [
            models.Index(fields=['is_active'])
        ]

    objects = UserManager
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'is_staff']

    def __str__(self) -> str:
        """Return First, middle, and last names as strings
        """
        return self.email
    
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db.models import (
    CharField, EmailField, BooleanField
)


# User manager class
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and return an administrative or resident account
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """A helper function for the "create_user" function

            Help to create an adminstrative user account
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email: EmailField = models.EmailField(max_length=100, unique=True)
    is_staff: BooleanField = models.BooleanField(default=False)
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
    REQUIRED_FIELDS = 'email'

    def __str__(self) -> str:
        """Return First, middle, and last names as strings
        """
        return self.email
    
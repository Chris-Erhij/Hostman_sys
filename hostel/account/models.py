from django.db import models
from django.db.models import (
    Model, CharField, EmailField,
)


class User(Model):
    first_name: CharField = models.CharField(max_length=100, help_text="First name here")
    middle_name: CharField = models.CharField(max_length=100, help_text="middle name here", blank=True)
    last_name: CharField = models.CharField(max_length=100, help_text="last name here")
    email: EmailField = models.EmailField(max_length=100, unique=True)
    password: CharField = models.CharField(max_length=100, unique=True)
    role: CharField = models.CharField(max_length=50)

    class Meta:
        ordering = [
            'first_name', 'middle_name', 'last_name',
        ]
        indexes = [
            models.Index(fields=['role'])
        ]

    def __str__(self) -> str:
        """Return First, middle, and last names as strings
        """
        return F"User full name {self.first_name, self.middle_name, self.last_name}"
    
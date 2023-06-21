from django.contrib.auth.models import (
    AbstractUser, Group, Permission
)
from django.db import models
from django.db.models import CharField, ManyToManyField


class CustomeUser(AbstractUser):
    EMPTY = ''
    ADMIN = 'admin'
    RESIDENT = 'resident'

    CHOICES = [
        (EMPTY, ''),
        (ADMIN, 'Admin'),
        (RESIDENT, 'Resident'),
    ]
    is_admin: CharField = models.CharField(max_length=10)
    groups: ManyToManyField = models.ManyToManyField(Group, related_name="Custome_users")
    
    user_permissions: ManyToManyField = models.ManyToManyField(
        Permission,
        verbose_name = 'user permissions',
        blank=True,
        help_text = ('The permissions this user has.'),
        related_name ='customeuser_permissions',  # modified related_name
        related_query_name ='customeuser' # modified
        )

    class Meta:
        ordering = [
            '-email',
        ]
        indexes = [
            models.Index(fields=['is_active'])
        ]

    def __str__(self) -> str:
        """Return email, username, as strings in the Admin.
        """
        return self.email.__str__()
    
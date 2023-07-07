import django
from django.contrib.auth.models import (
    AbstractUser, Group, Permission
)
from django.db import models
from django.db.models import CharField, ManyToManyField, EmailField


class CustomeUser(AbstractUser):
    EMPTY = ''
    ADMIN = 'admin'
    RESIDENT = 'resident'

    CHOICES = [
        (EMPTY, ''),
        (ADMIN, 'Admin'),
        (RESIDENT, 'Resident'),
    ]
    username: CharField = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
    email: EmailField = models.EmailField(blank=False, unique=True)
    is_admin: CharField = models.CharField(max_length=10, default='')
    confirm_password: CharField = models.CharField(error_messages={'mismatch': 'Passwords do not match'}, max_length=128, null=True)

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
            '-date_joined',
        ]
        indexes = [
            models.Index(fields=['is_active'])
        ]

    def __str__(self) -> str:
        """Return username, as strings when queried.
        """
        return self.username.__str__()
    
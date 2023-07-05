from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomeUser


UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def add_user_to_group(sender, instance, created, **kwargs) -> None:
    """A signal handler function

       Function to automatically add a newly created user to a specific group
       after persisted to database. I.E. saved.
    """

    if created and instance.is_staff:
        group_name = "Hostel Admin"

        try:
            group = Group.objects.get(name=group_name)
            instance.groups.add(group)
        except Group.DoesNotExist:
            pass

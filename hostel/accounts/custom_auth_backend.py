from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import AbstractUser

UserModel = get_user_model()


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs) -> AbstractUser | None:
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            user = UserModel.objects.get(**kwargs)
        except UserModel.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        
    def get_user(self, user_id) -> None | AbstractUser:
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

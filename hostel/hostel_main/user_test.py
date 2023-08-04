from django.contrib.auth.decorators import user_passes_test
from accounts.models import CustomeUser


def users_non_users_allowed(user) -> CustomeUser | None:
    return user.is_anonymous or user.is_authenticated


def login_not_required(view_func):
    return user_passes_test(users_non_users_allowed, login_url=None)(view_func)

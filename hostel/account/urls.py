from django.urls import path
from . import views


app_name: str = 'account'
urlpatterns = [
    path('signup/', views.signup, name='signup-view'),
]

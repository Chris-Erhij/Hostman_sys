from django.urls import path
from . import views


app_name: str = 'accounts'
urlpatterns = [
    path('register/', views.signup, name='signup-view'),
    path('login/', views.signin, name='signin-view'),
    path('logout/', views.signout, name='signout-view'),
]

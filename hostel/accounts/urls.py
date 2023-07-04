from django.urls import path
from . import views


app_name: str = 'accounts'
urlpatterns = [
    path('admin/', views.admin_signin, name='admin-signin-view'),
    path('login/', views.signin, name='signin-view'),
    path('register/', views.signup, name='signup-view'),
    path('logout/', views.signout, name='signout-view'),
]

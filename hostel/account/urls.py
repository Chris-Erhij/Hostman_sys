from django.urls import path
from . import views


app_name: str = 'account'
urlpatterns = [
    path('signup/', views.account_detail, name='account-detail'),
]

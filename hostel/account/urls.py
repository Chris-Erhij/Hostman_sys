from django.urls import path
from . import views


app_name: str = 'account'
urlpatterns = [
    path('dash/', views.account_detail, name='account-detail'),
]

from django.urls import path
from . import views


app_name: str = 'booking'
urlpatterns = [
    path('', views.booking_detail, name='booking-detail'),
]

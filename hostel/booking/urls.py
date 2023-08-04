from django.urls import path
from . import views


app_name: str = 'booking'
urlpatterns = [
    path('create/<int:id>/', views.booking_create, name='booking-create-view'),
    path('detail/', views.booking_detail, name='booking-detail-view'),
]

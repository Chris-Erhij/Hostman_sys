from django.urls import path
from . import views

app_name: str = 'hostel_main'
urlpatterns = [
    path('guest/', views.guest_view, name='home-guest-view'),  # Guest.
    path('resident/dash/', views.resident_dash, name='resident-dash-view'),  # Logged in as resident.
    path('hostel-detail/<str:id>/', views.hostel_detail, name='hostel-detail')
]

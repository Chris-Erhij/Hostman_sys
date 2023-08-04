from django.urls import path
from . import views

app_name: str = 'hostel_main'
urlpatterns = [
    path('guest/', views.guest_view, name='home-guest-view'),  # Guest.
    path('resident/dash/', views.resident_dash, name='resident-dash-view'),  # Logged in as resident.
    path('detail/hostel/<int:id>/', views.hostel_detail, name='hostel-detail-view'),
    path('detail/room/<int:id>/', views.room_detail, name='room-detail-view'),
    path('all-available-hostels/', views.list_hostel, name='list-hostel-view'),
    path('all-available-rooms/', views.list_room, name='list-room-view')
]

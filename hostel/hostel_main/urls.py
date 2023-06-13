from django.urls import path
from . import views

app_name: str = 'hostel_main'
urlpatterns = [
    path('', views.index_view, name='index-view'),
]

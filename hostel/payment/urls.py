from django.urls import path
from . import views

app_name: str = 'payment'
urlpatterns = [
    path('make/', views.make_payment, name='make-payment-view'),
    path('success/', views.pay_success, name='pay-success-view'),
    path('canceled/', views.pay_cancel, name='pay-cancel-view'),
]

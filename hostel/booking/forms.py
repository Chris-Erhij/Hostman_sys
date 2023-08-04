from django.forms import ModelForm
from booking.models import Booking


class BookingCreateForm(ModelForm):
    class Meta:
        model = Booking
        fields = [
        'first_name', 'last_name', 'email', 'check_in_date',
        'check_out_date', 'booking_option'
        ]

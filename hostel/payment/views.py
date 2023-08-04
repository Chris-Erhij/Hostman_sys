from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from hostel_main import user_test
from booking.models import Booking


def make_payment(request: HttpRequest) -> HttpResponse:  # type: ignore
    """ Paystack integration
    """
    pass


@user_test.login_not_required
def pay_success(request: HttpRequest) -> HttpResponse:
    user = request.user
    booking_id = None

    if user.is_authenticated:
        try:
            booking = user.booking  # type: ignore
            booking_id = booking.id

        except Booking.DoesNotExist:
            pass
        return render(request, "payment/success.html", {'user': user, 'booking_id': booking_id})
    
    else:
        try:
            booking_id = request.session.get('booking_id')
        except Booking.DoesNotExist:
            pass
        return render(request, 'payment/success.html', {'booking_id': booking_id})


@user_test.login_not_required
def pay_cancel(request: HttpRequest) -> HttpResponse:

    user = request.user
    return render(request, 'payment/cancel.html', {'user': user})

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .forms import BookingCreateForm
from .models import Booking
from hostel_main.models import HostelRooms
from hostel_main import user_test
from django.http import HttpResponseRedirect


@user_test.login_not_required
def booking_create(request: HttpRequest, id: int) -> HttpResponse | HttpResponseRedirect:
    room: HostelRooms = get_object_or_404(HostelRooms, pk=id)

    if not request.user.is_authenticated:
        status = "Anonymous"
    else:
        status = "Authenticated"

    if request.method == 'POST':
        form = BookingCreateForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room

            if status == "Anonymous":
                booking_data = {
                        "id": booking.id,
                        "first_name": form.cleaned_data['first_name'],
                        "last_name": form.cleaned_data['last_name'],
                        "email": form.cleaned_data['email'],
                        "check_in_date": form.cleaned_data['check_in_date'],
                        "check_out_date": form.cleaned_data['check_out_date'],
                        "booking_option": form.cleaned_data['booking_option']
                        }
                
                request.session["booking_data"] = booking_data
                request.session['booking_id'] = booking_data['id']

            else:
                user = request.user
                booking_data = request.session.get('booking_data', None)
                if booking_data:            
                    user.booking.create(    # type: ignore
                                            first_name=booking_data['first_name'],
                                            last_name=booking_data['last_name'],
                                            email=booking_data['email'],
                                            check_in_date=booking_data['check_in_date'],
                                            check_out_date=booking_data['check_out_date'],
                                            booking_option=booking_data['booking_option']
                                        )
                
                    del request.session['booking_data']
    else:
        form = BookingCreateForm()
    return render(request, 'booking/booking-create.html', locals())


@user_test.login_not_required
def booking_detail(request: HttpRequest) -> HttpResponse:
    user = request.user
    booking_id = None

    if user.is_authenticated:
        try:
            booking = user.booking  # type: ignore
            booking_id = booking.id
            
        except Booking.DoesNotExist:
            pass
        return render(request, 'booking/booking-detail.html', {'user': user, 'booking_id': booking_id})
    
    else:
        try:
            booking_id = request.session.get('booking_id', None)
        except Booking.DoesNotExist:
            pass
        return render(request, 'booking/booking-detail.html', {'booking_id': booking_id})
    
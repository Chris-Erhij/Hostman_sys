from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Hostel, HostelRooms


def guest_view(request: HttpRequest) -> HttpResponse:
    hostels = Hostel.objects.filter(available=True).order_by('-created')[:11]
    rooms = HostelRooms.objects.filter(is_occupied=False)[:11]

    context = {'hostels': hostels, 'rooms': rooms}
    return render(request, "hostel_main/base.html", context=context)


@login_required
def resident_dash(request: HttpRequest) -> HttpResponse:
    return render(request, "hostel_main/accommodation/resident_dash.html")

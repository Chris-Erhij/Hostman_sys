from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Hostel, HostelRooms
from accounts.models import CustomeUser


def guest_view(request: HttpRequest) -> HttpResponse:
    hostels = Hostel.objects.filter(available=True).order_by('-created')[:11]
    rooms = HostelRooms.objects.filter(is_occupied=False)[:11]

    context = {'hostels': hostels, 'rooms': rooms}
    return render(request, "hostel_main/base.html", context=context)


@login_required
def resident_dash(request: HttpRequest) -> HttpResponse:
    """ Return account holder only objects.

        As well as general objects for guest users.
    """

    try:
        hostels: Hostel = Hostel.objects.filter(available=True).order_by('-created')[:11]
    except Hostel.DoesNotExist:
        pass
    try:
        rooms: HostelRooms = HostelRooms.objects.filter(is_occupied=False, room_capacity__gte=1)[:11]
    except HostelRooms.DoesNotExist:
        raise Http404("Rooms does not exist")
    try:
        user: CustomeUser = request.user
    except CustomeUser.DoesNotExist:
        raise Http404("user does not exist") from None
            
    return render(request, "hostel_main/accommodation/resident_dash.html", locals())

@login_required or None
def hostel_detail(request: HttpRequest, id: int) -> HttpResponse:
    """ Return detail of a specific hostel using it"s ID
    """
    hostel = get_object_or_404(Hostel, pk=id, available=True)
    try:
        hostel_rooms: HostelRooms = hostel.rooms.all()
    except HostelRooms.DoesNotExist:
        raise Http404("Hostel has no rooms")
    
    return render(request, "hostel_main/accommodation/hostel-detail.html", {'hostel': hostel, 'hostel_rooms': hostel_rooms})

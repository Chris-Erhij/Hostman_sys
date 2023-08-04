from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Hostel, HostelRooms
from accounts.models import CustomeUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from booking.views import booking_create
from . import user_test


@user_test.login_not_required
def guest_view(request: HttpRequest) -> HttpResponse:
    user = request.user
    
    hostels = Hostel.objects.filter(available=True).order_by('-created')[:5]
    rooms = HostelRooms.objects.filter(is_occupied=False)[:5]

    context = {'hostels': hostels, 'rooms': rooms}
    return render(request, "hostel_main/base.html", context=context)


@login_required
def resident_dash(request: HttpRequest) -> HttpResponse:
    """ Return account holder only objects.

        As well as general objects for guest users.
    """
    try:
        hostels = Hostel.objects.filter(available=True).order_by('-created')[:5]
    except Hostel.DoesNotExist:
        pass
    try:
        rooms = HostelRooms.objects.filter(is_occupied=False, room_capacity__gte=1)[:5]
    except HostelRooms.DoesNotExist:
        raise Http404("Rooms does not exist")
    try:
        user = request.user
    except CustomeUser.DoesNotExist:
        raise Http404("user does not exist") from None
            
    return render(request, "hostel_main/accommodation/resident_dash.html", locals())


@user_test.login_not_required
def hostel_detail(request: HttpRequest, id: int) -> HttpResponse:
    """ Return detail of a specific hostel using it"s ID
    """
    user = request.user
    hostel = get_object_or_404(Hostel, pk=id)

    try:
        hostel_rooms = hostel.rooms.filter(is_occupied=False)  # type: ignore
    except HostelRooms.DoesNotExist:
        message: str = "Hostel has no available rooms at this time"
    
        return render(request, "hostel_main/accommodation/hostel-detail.html", {'message': message})
    return render(request, "hostel_main/accommodation/hostel-detail.html",
                    {
                        'hostel': hostel, 'hostel_rooms': hostel_rooms, 'user': user
                    })


@user_test.login_not_required
def room_detail(request: HttpRequest, id: int) -> HttpResponse:
    user = request.user

    room: HostelRooms = get_object_or_404(HostelRooms, pk=id)

    booking_create(request, id=room.id)  # type: ignore
    return render(request, "hostel_main/accommodation/room-detail.html", locals())


@user_test.login_not_required
def list_hostel(request: HttpRequest) -> HttpResponse:
    user = request.user

    list_hostel = Hostel.objects.filter(available=True)
    
    paginator = Paginator(list_hostel, 6)
    page_number = request.GET.get('page')

    try:
        hostels = paginator.page(page_number) # type: ignore
    except EmptyPage:
        hostels = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        hostels = paginator.page(1)

    context: dict = {'hostels': hostels, 'user': user}
    return render(request, 'hostel_main/accommodation/list-hostel.html', context)


@user_test.login_not_required
def list_room(request: HttpRequest) -> HttpResponse:
    user = request.user

    list_room = HostelRooms.objects.filter(is_occupied=False)

    paginator = Paginator(list_room, 6)
    page_number = request.GET.get('page')

    try:
        rooms = paginator.page(page_number) # type: ignore
    except EmptyPage:
        rooms = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        rooms = paginator.page(1)

    context: dict = {'rooms': rooms, 'user': user}
    return render(request, "hostel_main/accommodation/list-room.html", context)

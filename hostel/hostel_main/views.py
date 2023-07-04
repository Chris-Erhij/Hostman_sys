from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required


def guest_view(request: HttpRequest) -> HttpResponse:
    return render(request, "hostel_main/base.html")


@login_required
def resident_dash(request: HttpRequest) -> HttpResponse:
    return render(request, "hostel_main/accommodation/resident_dash.html")

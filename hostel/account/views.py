from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import User


def signup(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        # Handle form submission
        email = request.POST['email']
        password = request.POST['password']
        account_type  = request.POST['']

        # Create resident user
        resident_user = User.objects.create_user(
            email=email, password=password,
            )
        # Creat staff user
        admin_user = User.objects.create_superuser(
            email=email, password=password,
        )
        if resident_user:
            return render(request, "hostel_main/accommodation/resident_dash.html")
        if admin_user:
            return render(request, "hostel_main/accommodation/resident_dash.html")
        
        # Additional logic (e.g., redirect to login page)
    return render(request, 'signup.html')

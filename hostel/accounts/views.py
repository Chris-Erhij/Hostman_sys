from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import UserSignInForm, UserSignUpForm
from django.contrib.auth import login, logout, authenticate
from .models import CustomeUser
from django import forms
from django.urls import reverse


def signup(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False,)
            is_admin = form.cleaned_data['is_admin']
            user.is_admin = is_admin

            if user.is_admin == CustomeUser.ADMIN:
                user = CustomeUser.objects.create_superuser(form.cleaned_data['username'], form.cleaned_data['email'],
                                                       form.cleaned_data['password'])
                user.is_superuser = False

            else:
                user = CustomeUser.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                                       form.cleaned_data['password'])
            user.is_admin = is_admin
            user.save()

            if user.is_staff and user.is_admin == CustomeUser.ADMIN:
                messages.success(request=request, message="Admin account created successfully")
                return redirect("accounts:admin-signin-view")
            else:
                messages.success(request=request, message="Resident account created successfully")
                return redirect("accounts:signin-view")
        else:
            raise forms.ValidationError(message='Invalid credentials!, please try again')      
    else:     
        form = UserSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def signin(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        auth_form = UserSignInForm(request.POST)
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        user = authenticate(username=username_or_email, password=password)

        if user is not None and not user.is_staff:                
            login(request, user)
            messages.success(request=request, message="Successfully logged in as a Resident")
            return redirect("hostel_main:resident-dash-view")
        
        elif user is not None and user.is_staff:
            messages.success(request=request, message="Please use this admin signin form")
            return redirect("accounts:admin-signin-view")
        else:        
            messages.error(request=request, message="Invalid login credentials")
            return render(request, "accounts/signin.html", {'auth_form': auth_form})
    
    else:
        auth_form = UserSignInForm()
    return render(request, "accounts/signin.html", {'auth_form': auth_form})


def admin_signin(request: HttpRequest) -> HttpResponseRedirect:
    admin_login_url = reverse('admin:login')
    return redirect(admin_login_url)


def signout(request: HttpRequest) -> HttpResponseRedirect:
    logout(request)
    messages.success(request=request, message="Successfully signed out sign in again to continue")
    return redirect("accounts:signin-view")

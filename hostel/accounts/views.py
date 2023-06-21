from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import UserSignInForm, UserSignUpForm
from django.contrib.auth import login, logout
from .models import CustomeUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm

def signup(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False,)
            is_admin = form.cleaned_data['is_admin']
            user.is_admin = is_admin
            user.save()

            if user.is_admin == CustomeUser.RESIDENT:
                messages.success(request=request, message="Resident account created successfully")
                return redirect("accounts:signin-view")
            
            elif user.is_admin == CustomeUser.ADMIN:
                messages.success(request=request, message="Admin account created successfully")
                return redirect("accounts:signin-view")
        else:
            raise forms.ValidationError(message='Invalid credentials!, please try again')      
    else:     
        form = UserSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def signin(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        auth_form = UserSignInForm(request.POST)

        if auth_form.is_valid():
            email = auth_form.cleaned_data['email']
            password = auth_form.cleaned_data['password']

            user = CustomeUser.objects.get(email=email, password=password)
            if user:                
                if user.is_admin == CustomeUser.ADMIN:
                    request.session['next'] = "/home/admin/dash/"
                    login(request, user)

                    messages.success(request=request, message="Successfully logged in as an admin")
                    return redirect(request.session.get('next', '/'))
                
                else:
                    request.session['next'] = "/home/resident/dash/"
                    login(request, user)

                    messages.success(request=request, message="Successfully logged in as a resident")
                    return redirect(request.session.get('next', '/'))
            else:
                messages.error(request=request, message="User does not exit or Invalid username or password." \
                               "Please try again with correct credentials")
                return render(request, "accounts/signin.html", {'auth_form': auth_form})
        else:        
            messages.error(request=request, message="Invalid username or password")
        return render(request, "accounts/signin.html", {'auth_form': auth_form})
    
    else:
        auth_form = UserSignInForm()
    return render(request, "accounts/signin.html", {'auth_form': auth_form})


def signout(request: HttpRequest) -> HttpResponseRedirect:
    logout(request)
    messages.success(request=request, message="Successfully signed out sign in again to continue")
    return redirect("accounts:signin-view")

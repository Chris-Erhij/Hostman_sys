from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import User
from django.contrib import messages
from .forms import UserSignInForm, UserSignUpForm


def signup(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            # Create resident or admin user
            if cd['is_staff']:
                user = User.objects.create_user(
                    email=cd['email'], password=cd['password'], is_staff=cd['is_staff']
                    )
                
                # persist user to database
                user.save()

                return redirect('account:signin-view')
            else:
                raise ValueError(messages.error(message="You must select an account type!"))
        form = UserSignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def signin(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    pass

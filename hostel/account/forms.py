from django import forms
from django.forms import ModelForm, ModelChoiceField, BooleanField
from .models import User
from typing import Type


class UserSignUpForm(ModelForm):
    class Meta:
        model: Type = User
        fields: list[str] = [
            'email',
            'is_staff',
        ]


class UserSignInForm(ModelForm):
    class Meta:
        model: Type = User
        fields: list[str] = [
            'email',
        ]

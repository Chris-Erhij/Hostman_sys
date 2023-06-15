from django import forms
from django.forms import ModelForm, ModelChoiceField, BooleanField
from .models import User
from typing import Type


class UserSignUpForm(ModelForm):
    is_staff: ModelChoiceField = forms.ModelChoiceField(queryset=User.objects.all(),)
    is_active: BooleanField = forms.BooleanField(required=False, initial=True,
                                                 widget=forms.HiddenInput)
    class Meta:
        model: Type = User
        fields: list[str] = [
            'email',
            'is_staff',
            'is_active'
        ]


class UserSignInForm(ModelForm):
    class Meta:
        model: Type = User
        fields: list[str] = [
            'email',
        ]

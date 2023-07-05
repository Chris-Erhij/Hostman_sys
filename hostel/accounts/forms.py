from django import forms
from django.forms import ChoiceField, Form, ModelForm, CharField
from .models import CustomeUser
from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError

class UserSignUpForm(ModelForm):
    is_admin: ChoiceField = forms.ChoiceField(choices=CustomeUser.CHOICES, initial=CustomeUser.CHOICES[0], label="Account type", required=True)
    password: CharField = forms.CharField(min_length=8, widget=forms.PasswordInput, validators=[validate_password])    
    confirm_password: CharField = forms.CharField(min_length=8, widget=forms.PasswordInput, validators=[validate_password])

    class Meta:
        model = CustomeUser
        fields = [
            'username',
            'email',
            'password',
            'confirm_password',
            'is_admin'  
        ]
            
    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if (password and confirm_password) and (password != confirm_password):
            raise ValidationError(message='Password mismatch')
        return cleaned_data

    def save(self, commit=False):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if commit:
            user.set_password(password)
            user.save()
        return user


class UserSignInForm(Form):
    username_or_email: CharField = forms.CharField()
    password: CharField = forms.CharField(widget=forms.PasswordInput,)

    class Meta:
        model = CustomeUser
        fields = [
            'username_or_email',
            'password'
        ]
   
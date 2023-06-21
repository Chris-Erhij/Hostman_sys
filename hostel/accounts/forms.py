from django import forms
from django.forms import ChoiceField, ModelForm, EmailField, CharField
from .models import CustomeUser
from django.contrib.auth.password_validation import validate_password



class UserSignUpForm(ModelForm):
    password: CharField = forms.CharField(min_length=8, widget=forms.PasswordInput, validators=[validate_password])
    is_admin: ChoiceField = forms.ChoiceField(choices=CustomeUser.CHOICES, required=True, label='Account type', initial=CustomeUser.CHOICES[0])
    
    class Meta:
        model = CustomeUser
        fields = [
            'username',
            'email',
            'password',
            'is_admin'
        ]
            

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
    def save(self, commit=False):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')

        if commit:
            user.set_password(password)
            user.save()
        return user


class UserSignInForm(ModelForm):
    email: EmailField = forms.EmailField(help_text="Enter registration email")
    password: CharField = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])

    class Meta:
        model = CustomeUser
        fields = [
            'email',
            'password'
        ]
   
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# User = get_user_model()


class SignUpUserCreationForm(forms.Form):
        username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
        email = forms.EmailField(label='Enter email')
        password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

        def clean_username(self):
            username = self.cleaned_data['username'].lower()
            user = User.objects.filter(username=username)
            if user.count():
                raise ValidationError("Username already exists")
            return username

        def clean_email(self):
            email = self.cleaned_data['email'].lower()
            user = User.objects.filter(email=email)
            if user.count():
                raise ValidationError("Email already exists")
            return email

        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if password1 and password2 and password1 != password2:
                raise ValidationError("Password don't match")

            return password2

        def save(self, commit=True):
            user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password1']
            )
            return user

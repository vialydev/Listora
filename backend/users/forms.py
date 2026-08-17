from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Общие атрибуты для всех полей
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-input",
            })

        # Индивидуальные placeholder'ы
        self.fields["username"].widget.attrs.update({
            "placeholder": "Username",
        })

        self.fields["first_name"].widget.attrs.update({
            "placeholder": "Name",
        })

        self.fields["last_name"].widget.attrs.update({
            "placeholder": "Lastname",
        })

        self.fields["email"].widget.attrs.update({
            "placeholder": "Email",
        })

        self.fields["password1"].widget.attrs.update({
            "placeholder": "Password",
        })

        self.fields["password2"].widget.attrs.update({
            "placeholder": "Confirm password",
        })



class UserLoginForm(forms.Form):

    username_or_email = forms.CharField(
        max_length=254,
        label="Username or Email",
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password",
    )

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.request = request

        self.fields["username_or_email"].widget.attrs.update({
            "class": "form-input",
            "placeholder": "Username or Email",
        })

        self.fields["password"].widget.attrs.update({
            "class": "form-input",
            "placeholder": "Password",
        })

    def clean(self):
        cleaned_data = super().clean()

        username_or_email = cleaned_data.get("username_or_email")
        password = cleaned_data.get("password")

        if not username_or_email or not password:
            return cleaned_data

        user = authenticate(
            self.request,
            username=username_or_email,
            password=password,
        )

        if user is None:
            raise forms.ValidationError(
                "Invalid username/email or password."
            )

        self.user = user

        return cleaned_data

    def get_user(self):
        return self.user
from django import forms
from django.contrib.auth.forms import UserCreationForm

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
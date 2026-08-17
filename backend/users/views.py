from urllib import request
from django.http import HttpResponse
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.shortcuts import redirect

from .forms import UserRegisterForm, UserLoginForm
from .models import User



class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:register")



class LoginView(FormView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("users:register")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        user = form.get_user()

        login(self.request, user)

        return super().form_valid(form)



def LogoutView(request):
    logout(request)
    return redirect("login")
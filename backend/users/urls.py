from django.urls import path

from .views import RegisterView, LoginView, LogoutView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView, name="logout")
    # path("home/", HomeView, name="home")
]
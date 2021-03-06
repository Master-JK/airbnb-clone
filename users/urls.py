from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    # path("logout", views.logout_view, name="logout"),
    path("logout", views.Logout_View.as_view(), name="logout"),
    path("signup", views.SingUpView.as_view(), name="signup"),
]

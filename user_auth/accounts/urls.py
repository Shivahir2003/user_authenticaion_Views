from django.urls import path,include
from django.contrib.auth import views as auth_views
from accounts.views import index,signupview,dashboard

urlpatterns = [
    path("index/", index, name='index'),
    path("accounts/login/",auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('accounts/profile/', dashboard, name='dashboard'),
    path("accounts/signup/",signupview,name='signup'),
    path("accounts/", include("django.contrib.auth.urls")),
]
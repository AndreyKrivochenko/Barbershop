from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render

from authapp.forms import ShopUserLoginForm


class ShopLogoutView(LogoutView):
    next_page = 'mainapp/index.html'


class ShopLoginView(LoginView):
    authentication_form = ShopUserLoginForm
    success_url = 'mainapp/index.html'
    template_name = 'authapp/login.html'

from django.contrib.auth.forms import AuthenticationForm

from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'password')

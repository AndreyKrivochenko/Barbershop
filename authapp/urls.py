from django.urls import path

from authapp.views import ShopLogoutView, ShopLoginView

app_name = 'authapp'

urlpatterns = [
    path('login/', ShopLoginView.as_view(), name='login'),
    path('logout/', ShopLogoutView.as_view(), name='logout')
]

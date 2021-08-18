from django.urls import path

from mainapp.views import IndexView, ContactView, AboutView

app_name = 'mainapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
]

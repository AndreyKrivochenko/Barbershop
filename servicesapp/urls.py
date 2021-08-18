from django.urls import path

from servicesapp.views import ServicesView

app_name = 'servicesapp'

urlpatterns = [
    path('', ServicesView.as_view(), name='services')
]

from django.urls import path

from servicesapp.views import ServicesView, ServiceDetailView

app_name = 'servicesapp'

urlpatterns = [
    path('', ServicesView.as_view(), name='services'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service_detail')
]

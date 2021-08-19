from django.views.generic import TemplateView, DetailView

from .models import ServicesCategories, Services


class ServicesView(TemplateView):
    template_name = 'servicesapp/services.html'

    def get_context_data(self, **kwargs):
        data = super(ServicesView, self).get_context_data(**kwargs)
        data['categories'] = ServicesCategories.get_categories()
        data['services'] = Services.get_services()
        return data


class ServiceDetailView(DetailView):
    model = Services
    template_name = 'servicesapp/service_single.html'

    def get_context_data(self, **kwargs):
        data = super(ServiceDetailView, self).get_context_data(**kwargs)
        service_pk = self.kwargs['pk']
        print(self.kwargs)

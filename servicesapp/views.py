from django.views.generic import TemplateView


class ServicesView(TemplateView):
    template_name = 'servicesapp/services.html'

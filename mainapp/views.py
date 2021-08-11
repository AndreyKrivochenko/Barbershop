from django.http import HttpResponseNotFound
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class ContactView(TemplateView):
    template_name = 'mainapp/contact.html'


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
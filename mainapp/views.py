from django.http import HttpResponseNotFound
from django.views.generic import TemplateView

from mainapp.models import MainGallery, MainSlider, AboutUs


class IndexView(TemplateView):
    model = MainGallery, MainSlider
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        data = super(IndexView, self).get_context_data(**kwargs)
        gallery = MainGallery.objects.all()
        slider = MainSlider.objects.all()
        data['gallery'], data['slider'] = gallery, slider
        return data


class ContactView(TemplateView):
    template_name = 'mainapp/contact.html'


class AboutView(TemplateView):
    template_name = 'mainapp/about.html'

    def get_context_data(self, **kwargs):
        data = super(AboutView, self).get_context_data(**kwargs)
        accordion = AboutUs.objects.all()[0]
        data['accordion'] = accordion
        return data


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
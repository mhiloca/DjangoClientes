from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Olá Mundo, estou de volta ao Django'
        return context


class MyView(View):
    template_name = 'home4.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'home4.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'home4.html')


def home(request):
    return render(request, 'home.html')


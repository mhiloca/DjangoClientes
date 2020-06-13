from django.urls import path
from django.views.generic.base import TemplateView

from .views import home, HomePageView, MyView


urlpatterns = [
    path('', home, name='home'),
    path('home2', TemplateView.as_view(template_name='home2.html')),
    path('home3', HomePageView.as_view()),
    path('home4', MyView.as_view())
]
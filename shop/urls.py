from django.urls import path
from . import views
from .forms import ContactForm

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
]
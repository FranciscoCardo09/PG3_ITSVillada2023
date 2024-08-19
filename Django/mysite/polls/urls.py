from django.urls import path
from . import views
from .views import ejercicio2

urlpatterns = [
    path('', views.home, name='home'),
    path('ejercicio2/', ejercicio2.as_view(), name='ejercicio2'),
]
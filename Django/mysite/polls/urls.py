from django.urls import path
from . import views
from .views import ejercicio2, AutorCreateView, LibroCreateView, PrestamoCreateView, TablaView

urlpatterns = [
    path('', views.home, name='home'),
    path('ejercicio2/', ejercicio2.as_view(), name='ejercicio2'),
    path('autor/nuevo/', AutorCreateView.as_view(), name='crear_autor'),
    path('libro/nuevo/', LibroCreateView.as_view(), name='crear_libro'),
    path('prestamo/nuevo/', PrestamoCreateView.as_view(), name='crear_prestamo'),
    path('tabla/', TablaView.as_view(), name='tabla'),
]
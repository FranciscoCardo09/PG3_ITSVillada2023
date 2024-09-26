import requests
from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    try:
        api_url = 'https://reqres.in/api/users'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            user_list = data.get('data', [])

            campos = request.GET.getlist('fields')
            busqueda = request.GET.get('search', '')
            cant_users = int(request.GET.get('user_count', len(user_list)))  

            if busqueda:
                user_list = [user for user in user_list if busqueda.lower() in user['first_name'].lower() or 
                                                             busqueda.lower() in user['last_name'].lower() or 
                                                             busqueda.lower() in user['email'].lower()]

            user_list = user_list[:cant_users]

            return render(request, "index.html", {'user_list': user_list, 'selected_fields': campos, 'search_query': busqueda, 'user_count': cant_users})
        else:
            return render(request, "error.html", {'message': 'Error al obtener datos de la API'})
    except Exception as e:
        return render(request, "error.html", {'message': str(e)})

class ejercicio2(TemplateView):
    template_name = "ejercicio2.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        res = requests.get("https://www.cultura.gob.ar/api/v2.0/museos/")
        res_json = res.json()
        museos_res = res_json.get('results')
        context['museos'] = museos_res
        return context
    
from django.views.generic import TemplateView, FormView
from django.urls import reverse
from .forms import AutorForm, LibroForm
from .models import Autor, Libro

class AutorCreateView(FormView):
    template_name = 'autor_form.html'
    form_class = AutorForm

    def get_success_url(self):
        return reverse('crear_libro')
    
    def form_valid(self, form):
        form.save()  
        return super().form_valid(form)

class LibroCreateView(FormView):
    template_name = 'libro_form.html'
    form_class = LibroForm
    
    def get_success_url(self):
        return reverse('crear_prestamo')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

from .forms import PrestamoForm
    
class PrestamoCreateView(FormView):
    template_name = 'prestamo_form.html'
    form_class = PrestamoForm

    def get_success_url(self):
        return reverse('tabla')

    def form_valid(self, form):
        form.save()  
        return super().form_valid(form)
    
from .models import Autor, Libro, Prestamo

class TablaView(TemplateView):
    template_name = 'tabla.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autores'] = Autor.objects.all()
        context['libros'] = Libro.objects.all()
        context['prestamos'] = Prestamo.objects.all()
        return context
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
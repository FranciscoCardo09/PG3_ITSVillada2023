# Trabajo Practico Número 3: Consultas de Apis con Django

## Índice
1. [Descripción de la API](#descripción-de-la-api-reqres)
2. [Configuración Inicial](#2-configuración-inicial)
3. [Cambios](#3-cambios)
4. [Ejecutar](#4-ejecutar)
5. [Bibliografía](#bibliografía)


## 1. Descripción de la API: ReqRes
ReqRes es un servicio web que proporciona una API pública para propósitos de desarrollo y pruebas. Esta API simula un sistema de gestión de usuarios, permitiendo realizar operaciones básicas como listar usuarios, agregar nuevos usuarios, actualizar información de usuarios, entre otras.

## 2. Configuración Inicial

1. **Estructura del Proyecto:**
    - Se creó la estructura básica del proyecto Django con aplicaciones y archivos necesarios.

2. **Vista Inicial:**
    - Se configuró una vista (`home`) en `polls/views.py` para consumir una API (originalmente `https://reqres.in/api/users`) y mostrar los datos en una plantilla HTML.

3. **Plantilla HTML:**
    - Se creó una plantilla HTML (`template/index.html`) para mostrar la lista de usuarios. Y un HTML (`template/error.html`) para ir probando si sale algun error


## 3. Cambios

1. **Vista Actualizada:**
    - La vista en `polls/views.py` se actualizó para manejar los campos seleccionados por el usuario y pasar estos datos a la plantilla HTML.

```python
    import requests
    from django.shortcuts import render

    def home(request):
        try:
            api_url = 'https://reqres.in/api/users'
            response = requests.get(api_url)
            
            if response.status_code == 200:
                data = response.json()
                lista = data.get('data', [])

                campos = request.GET.getlist('fields')
                busqueda = request.GET.get('search', '')
                cant_users = int(request.GET.get('user_count', len(lista)))  

                if busqueda:
                    lista = [user for user in lista if busqueda.lower() in user['first_name'].lower() or 
                                                                busqueda.lower() in user['last_name'].lower() or 
                                                                busqueda.lower() in user['email'].lower()]

                lista = lista[:cant_users]

                return render(request, "index.html", {'lista': lista, 'selected_fields': campos, 'search_query': busqueda, 'user_count': cant_users})
            else:
                return render(request, "error.html", {'message': 'Error al obtener datos de la API'})
        except Exception as e:
            return render(request, "error.html", {'message': str(e)})
```


2. **Plantilla HTML:**
    - `template/index.html` se actualizó para incluir checkboxes que permiten al usuario seleccionar qué campos mostrar en la tabla. Y un input para que ingrese la cantidad

```html
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista Usuarios</title>
</head>
<body>
    <h1>Lista Usuarios</h1>

    <form method="get">
        <div>
            <label for="search">Buscar: </label>
            <input type="text" id="search" name="search" value="{{ search_query }}">
            <button type="submit">Buscar</button>
        </div>
        <div>
            <label for="user_count">Cantidad de Usuarios: </label>
            <input type="number" id="user_count" name="user_count" value="{{ user_count }}" min="1" max="100">
        </div>
        <div>
            <label><input type="checkbox" name="fields" value="id" {% if 'id' in selected_fields %}checked{% endif %}> ID</label>
            <label><input type="checkbox" name="fields" value="email" {% if 'email' in selected_fields %}checked{% endif %}> Email</label>
            <label><input type="checkbox" name="fields" value="first_name" {% if 'first_name' in selected_fields %}checked{% endif %}> Nombre</label>
            <label><input type="checkbox" name="fields" value="last_name" {% if 'last_name' in selected_fields %}checked{% endif %}> Apellido</label>
            <label><input type="checkbox" name="fields" value="avatar" {% if 'avatar' in selected_fields %}checked{% endif %}> Avatar</label>
            <button type="submit">Mostrar</button>
        </div>
    </form>
</body>
</html>
```


3. **Creación de Tabla:**
    - `template/index.html` Se le agregó una tabla para que muestre los usuarios con su ID, Nombre, Apellido, Email y Avatar. 

```html
   <table>
        <thead>
            <tr>
                {% if 'id' in selected_fields %}<th>ID</th>{% endif %}
                {% if 'email' in selected_fields %}<th>Email</th>{% endif %}
                {% if 'first_name' in selected_fields %}<th>Nombre</th>{% endif %}
                {% if 'last_name' in selected_fields %}<th>Apellido</th>{% endif %}
                {% if 'avatar' in selected_fields %}<th>Avatar</th>{% endif %}
            </tr>
        </thead>
        <tbody>
            {% for user in user_list %}
                <tr>
                    {% if 'id' in selected_fields %}<td>{{ user.id }}</td>{% endif %}
                    {% if 'email' in selected_fields %}<td>{{ user.email }}</td>{% endif %}
                    {% if 'first_name' in selected_fields %}<td>{{ user.first_name }}</td>{% endif %}
                    {% if 'last_name' in selected_fields %}<td>{{ user.last_name }}</td>{% endif %}
                    {% if 'avatar' in selected_fields %}<td><img src="{{ user.avatar }}" alt="Avatar" width="50"></td>{% endif %}
                </tr>
            {% endfor %}
        </tbody>
    </table>
```

## 4. Ejecutar

Se ejecuta el archivo para probar si esta todo bien hecho y que funcione.

```bash
    python manage.py migrate
```

## Bibliografia
## Bibliografía

1. **Django Documentation**
   - **Enlace**: [Django Documentation](https://docs.djangoproject.com/en/stable/)
   - **Descripción**: La documentación oficial de Django que proporciona una guía completa sobre cómo utilizar el framework Django para desarrollar aplicaciones web robustas.

2. **ReqRes API Documentation**
   - **Enlace**: [ReqRes API Documentation](https://reqres.in/)
   - **Descripción**: Documentación de la API de ReqRes, que ofrece una API pública para propósitos de desarrollo y pruebas, simulando un sistema de gestión de usuarios.

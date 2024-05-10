import requests
from weasyprint import HTML

def obtener_usuarios():
    response = requests.get("https://reqres.in/api/users")
    data = response.json()["data"]
    return data

def generar_tabla(usuarios):
    tabla = "| ID | Email | Nombre | Avatar |\n"
    tabla += "| --- | --- | --- |\n"

    for usuario in usuarios:
        tabla += f"| {usuario['id']} | {usuario['email']} | {usuario['first_name']} {usuario['last_name']} | ![Avatar]({usuario['avatar']}) |\n"

    return tabla

if __name__ == "__main__":
    usuarios = obtener_usuarios()
    tabla = generar_tabla(usuarios)

    html = f"<pre>{tabla}</pre>"

    HTML(string=html).write_pdf("usuarios.pdf")

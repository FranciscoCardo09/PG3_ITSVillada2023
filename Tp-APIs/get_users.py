import requests

response = requests.get("https://reqres.in/api/users")
usuario = response.json()["data"]

filtrar = [user for user in usuario if len(user["first_name"]) > 5]

for usuarios in filtrar:
    print(usuarios)

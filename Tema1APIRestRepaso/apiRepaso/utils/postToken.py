import requests

url = "http://localhost:5050/users"  
usuario = {"username":"Pepin2", "password":"123"}
response = requests.get(url, json=usuario)
tokenJson = response.json()
token = tokenJson['token']

url = "http://127.0.0.1:5050/personas" 
persona = {
    "id": 41,
    "nombre": "Fernando41",
    "apellidos": "Galinda",
    "direccion": "Mi casa",
    "telefono": "665876895",
    "idDepartamento": 1
}

tokenAuthorization = {"Authorization":f"Bearer {token}"}
response = requests.post(url, json=persona, headers=tokenAuthorization)
if response.status_code == 201:
    print("Persona publicada con exito")
else:
    print(f"Error: {response.status_code}\n{response.text}")

import requests

url="http://127.0.0.1:5050/personas"

id=7

url+="/"+str(id)

response=requests.delete(url)

if response.status_code == 200:
        print("Se ha borrado persona correctamente, codigo:", response.status_code)
else:
        print("La peticion no ha terminado correctamente, codigo:", response.status_code)
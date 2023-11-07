import requests 

url="http://localhost:5050/countries"

dict={"name": "España", "capital": "Madrid", "area": 555555}

response=requests.post(url, json=dict)

if response.status_code==201:
    print("Se ha creado el post correctamente, codigo:", response.status_code)
    
else:print("La peticion no ha terminado correctamente, codigo:", response.status_code)  
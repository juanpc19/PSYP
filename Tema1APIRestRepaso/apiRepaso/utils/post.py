import requests 

url="http://127.0.0.1:5050/personas"

dict={"id":6,"nombre":"Pepin","apellidos":"saza","direccion":"danuvio","telefono":"678343000","idDepartamento":2}

response=requests.post(url, json=dict)

if response.status_code==201:
    print("Se ha creado el post correctamente, codigo:", response.status_code)
else:
    print("La peticion no ha terminado correctamente, codigo:", response.status_code)
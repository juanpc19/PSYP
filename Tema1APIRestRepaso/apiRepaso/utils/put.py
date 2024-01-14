import requests

url="http://127.0.0.1:5050/personas"
 
id=5

dict={"nombre":"put","apellidos":"saza","direccion":"danuvio","telefono":"678343000","idDepartamento":2}

url+="/"+str(id)

response=requests.put(url, json=dict)

if response.status_code == 200:
        print("Se ha modificado persona correctamente, codigo:", response.status_code)
else:
        print("La peticion no ha terminado correctamente, codigo:", response.status_code)
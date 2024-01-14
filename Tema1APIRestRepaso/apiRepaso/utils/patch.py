import requests

url="http://127.0.0.1:5050/personas"
 
id=6

dict={"apellidos":"patch2"}

url+="/"+str(id)

response=requests.patch(url, json=dict)

if response.status_code == 200:
        print("Se ha modificado parcialmente persona correctamente, codigo:", response.status_code)
else:
        print("La peticion no ha terminado correctamente, codigo:", response.status_code)
import requests 

url="http://localhost:5050/countries"

id=3

url+="/"+str(id)

dict={"name": "paisReemplazo"}
    
#guardare la respuesta de la peticion put de un recurso en concreto a la url en response
response=requests.patch(url, json=dict)
    
#si la respuesta da codigo 200 (ok)
if response.status_code==200:
    print("Se ha parcheado el post correctamente, codigo:", response.status_code)
   
#si el codigo devuelto por response no es 200 comunico error de peticion con print 
else:print("La peticion no ha terminado correctamente, codigo:", response.status_code)
import requests 

url="http://localhost:5050/countries"

id="1"

url+="/"+id
    
#guardare la respuesta de la peticion put de un recurso en concreto a la url en response
response=requests.delete(url)
    
#si la respuesta da codigo 200 (ok)
if response.status_code==200:
    print("Se ha borrado el post correctamente, codigo:", response.status_code)
   
#si el codigo devuelto por response no es 200 comunico error de peticion con print 
else:print("La peticion no ha terminado correctamente, codigo:", response.status_code)
import requests 

url="http://127.0.0.1:5050/tiendas"

dict={
    "domicilio": "11111", "telefono": 686868689, "precioAlquiler": 900
    }

response=requests.post(url, json=dict)

if response.status_code==201:
    print("Se ha creado el post correctamente, codigo:", response.status_code)
    
else:print("La peticion no ha terminado correctamente, codigo:", response.status_code)  
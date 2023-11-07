import requests
api_url="https://jsonplaceholder.typicode.com/todos/5"

#guardo en dict lo datos a guardar
dict={"userId":2}
#guardo en response lo que me devuelve la request de patch al diccionario dict qu esta guardado en el json en la url api_url
response=requests.patch(api_url, json=dict)

#print de la respuesta
print("codigo de estado:", response.status_code)
print(response.json)
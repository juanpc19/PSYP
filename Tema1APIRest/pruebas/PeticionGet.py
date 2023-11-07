import requests
api_url="https://jsonplaceholder.typicode.com/todos/150"
#api_url="https://jsonplaceholder.typicode.com/users/1/todos/?id=11"

respuesta=requests.get(api_url)

print ("codigo estado:", respuesta.status_code)
print(respuesta.json())


import requests
api_url="https://jsonplaceholder.typicode.com/todos/5"

dict={"userId":2, "titulo": "hacer tareas", "completed": False}
response=requests.delete(api_url)

print("codigo de estado:", response.status_code)
print(response.json)
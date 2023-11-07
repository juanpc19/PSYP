import requests
api_url="https://jsonplaceholder.typicode.com/todos/5"

dict={"userId":2, "titulo": "hacer tareas", "completed": False}
response=requests.put(api_url, json=dict)

print("codigo de estado:", response.status_code)
print(response.json)
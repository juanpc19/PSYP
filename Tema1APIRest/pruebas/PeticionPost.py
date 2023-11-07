import requests
api_url="https://jsonplaceholder.typicode.com/users/1/todos/?id=11"

dict={"userId":2, "titulo": "hacer tareas", "completed": False}
response=requests.post(api_url, json=dict)

print(response.json)
print("codigo de estado:", response.status_code)

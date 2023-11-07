#todo el modulo copiado de elena

from utils.funciones import *

from flask import Blueprint, jsonify

ficheroCities = "../proyectoPaises/ficheros/cities.json"

#ficheroCities = "proyectoPaises\ficheros\cities.json"

#ficheroCities = "C:\Users\juanp\OneDrive\Documentos\GitHub\Tema1APIRest\proyectoPaises\ficheros\cities.json"

citiesBP = Blueprint('cities', __name__)

@citiesBP.get('/')
def get_cities():
    cities = leerFichero(ficheroCities)
    return jsonify(cities)

@citiesBP.get("/<int:id>")
def get_city(id):
    cities = leerFichero(ficheroCities)
    for city in cities:
        if city['id'] == id:
            return city, 200
    return {"error": "City not found"}, 404
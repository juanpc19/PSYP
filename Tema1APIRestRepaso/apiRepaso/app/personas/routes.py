import json
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

ficheroPersonas = "Tema1APIRestRepaso\\apiRepaso\\ficheros\\personas.json"
#ficheroPersonas = "Tema1APIRestRepaso/apiRepaso/ficheros/personas.json"
#ambas rutas funcionan

personasBP=Blueprint("personas", __name__)

#funcion que guarda abre nombreFichero en modo lectura guardando esta lectura en archivo lo cual me permite leer o modificar el archivo desde python, 
# carga el objeto creado (archivo) en tiendas en formato json,
# cierra el archivo y devuelve el contenido del mismo que ahora esta en tiendas en el return
def leerFichero(nombreFichero):
    archivo = open(nombreFichero, "r") 
    tiendas = json.load(archivo)
    archivo.close()
    return tiendas

#funcion que recibe un diccionario abre nombreFichero en modo escritura guardando esta escritura en archivo lo cual me permite leer o modificar el archivo desde python,
# sobreescribe el objeto creado (archivo) con los valores de tiendas (el diccionario con valor/valores de turno) y cierra el archivo
def escribeFichero(nombreFichero, tiendas):
    archivo = open(nombreFichero, "w")
    json.dump(tiendas,archivo)
    archivo.close()
    
def _find_Next_Id():
    personas = leerFichero(ficheroPersonas)
    return max(persona["id"] for persona in personas)+1 

@personasBP.get("/")
def getPersonas():
    personas=leerFichero(ficheroPersonas)
    return jsonify(personas)
    
@personasBP.get("/<int:id>")
def getPersona(id):
    personas=leerFichero(ficheroPersonas)
    
    for persona in personas:
        if persona["id"]==id:
            
            return persona, 200
    return {"Error:": "Persona no encontrada"}, 404

@personasBP.post("/")
@jwt_required()
def addPersona():
    personas=leerFichero(ficheroPersonas)
    
    if request.is_json:
        persona=request.get_json()
        persona["id"]=_find_Next_Id()
        personas.append(persona)
        personas=escribeFichero(ficheroPersonas,personas)
        
        return persona, 201
    
    return {"Error:":"La peticion debe ser JSON"}, 415

@personasBP.put("/<int:id>")
@personasBP.patch("/<int:id>")#usa mismo codigo uqe put por logica similar
def modificarPersona(id):
    personas=leerFichero(ficheroPersonas)
    
    if request.is_json:
        nuevaPersona=request.get_json()
        
        for persona in personas:
            if persona["id"]==id:
                for campo in nuevaPersona:
                    persona[campo]=nuevaPersona[campo]
        
                escribeFichero(ficheroPersonas,personas)
        
                return persona, 200
    return {"Error:": "La peticion debe ser JSON"}, 415

@personasBP.delete("/<int:id>")
def borrarPersona(id):
    personas=leerFichero(ficheroPersonas)
    
    for persona in personas:
        if persona["id"]==id:
            personas.remove(persona)
            escribeFichero(ficheroPersonas, personas)
            
            return "{}", 200
        
    return{"Error:": "Persona no encontrada"}, 404




    

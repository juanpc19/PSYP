import json
import bcrypt
from flask import Blueprint, request
from flask_jwt_extended import create_access_token

ficheroUsers="Tema1APIRestRepaso\\apiRepaso\\ficheros\\users.json"

usersBP=Blueprint("users", __name__)

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
    
@usersBP.post("/")
def registrarUser():
    users=leerFichero(ficheroUsers)
    
    if request.is_json:
        
        user=request.get_json()
        
        password= user["password"].encode("utf-8")
        
        sal=bcrypt.gensalt()
        
        hashPass=bcrypt.hashpw(password, sal).hex()
        
        user["password"]=hashPass   
        
        users.append(user)
        
        escribeFichero(ficheroUsers, users)
        
        token=create_access_token(identity=user["username"])
        
        return {"token": token}, 201
    
    return {"error": "Request must be JSON"}, 415
        
@usersBP.get("/")
def loginUser():
    users=leerFichero(ficheroUsers)
    
    if request.is_json:
        user=request.get_json()
        username=user["username"]
        password=user["password"].encode("utf-8")
        
        for userFile in users:
            if userFile["username"]==username:
                passwordFile=userFile["password"]
                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token=create_access_token(identity=username)
                    return {"token": token}, 200
                
                
                return {"Error" : "Contraseña erronea, no tiene permiso: "}, 401
            
        return {"Error: ": "El usuario no existe"}, 404
    
    return {'error': 'request must be JSON '}, 415

        
        
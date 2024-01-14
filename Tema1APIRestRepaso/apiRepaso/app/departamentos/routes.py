import json
from flask import Blueprint, jsonify, request

ficheroDepartamentos="Tema1APIRestRepaso\\apiRepaso\\ficheros\\departamentos.json"
ficheroPersonas = "Tema1APIRestRepaso\\apiRepaso\\ficheros\\personas.json"

departamentosBP=Blueprint("departamentos", __name__)


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
    departamentos = leerFichero(ficheroDepartamentos)
    return max(departamento["id"] for departamento in departamentos)+1 

 

@departamentosBP.get("/")
def getAllDepartamentos():
    departamentos=leerFichero(ficheroDepartamentos)
    
    return jsonify(departamentos)
    
@departamentosBP.get("/<int:id>")
def getDepartamento(id):
    departamentos=leerFichero(ficheroDepartamentos)
    
    for departamento in departamentos:
        if departamento["id"]== id:
            return departamento, 200
        
    return {"Error:" : "Departamento no encontrado"}, 404

@departamentosBP.post("/")
def crearDepartamento():
    departamentos=leerFichero(ficheroDepartamentos)
    
    if request.is_json:
        
        departamento=request.get_json()
        departamento["id"]=_find_Next_Id()
        
        departamentos.append(departamento)
        escribeFichero(ficheroDepartamentos, departamentos)
        
        return departamento, 201
    
    return {"Error:":"La peticion debe ser JSON"}, 415
    
@departamentosBP.put("/<int:id>")
@departamentosBP.patch("/<int:id>")
def modificarDepartamento(id):
    departamentos=leerFichero(ficheroDepartamentos)
    
    if request.is_json:
        departamentoModificado=request.get_json()
        
        for departamento in departamentos:
            if departamento["id"]==id:
                for x in departamento:
                    departamento[x]=departamentoModificado[x]
    
                escribeFichero(ficheroDepartamentos,departamentos)
        
                return departamentoModificado, 200
    
    return {"Error:":"La peticion debe ser JSON"}, 415

@departamentosBP.delete("/<int:id>")
def borrarDepartamento(id):
    departamentos=leerFichero(ficheroDepartamentos)
    
    for departamento in departamentos:
        if departamento["id"]==id:
            departamentos.remove(departamento)
            
            escribeFichero(ficheroDepartamentos, departamentos)
    
            return "{}", 200
    
    return {"Error:" : "Departamento no encontrado"}, 404

#anidado
@departamentosBP.get("/<int:id>/personas")
def getPersonaDepartamento(id):
    listaPersonasDep=[]
    personas=leerFichero(ficheroPersonas)
    
    for persona in personas:
        if persona["idDepartamento"]==id:
            listaPersonasDep.append(persona)
            
    if len(listaPersonasDep)>0:
        return listaPersonasDep, 200
    else:
        return {"Error:" : "No hay personas en ese departamento"}, 404
    
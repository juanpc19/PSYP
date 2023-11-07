
from utils.funciones import leerFichero, escribeFichero

#necesito blueprint para rutas y funciones y jsonify para formato
from flask import Blueprint, jsonify, request

from flask_jwt_extended import jwt_required

ficheroTiendas="../tareaApiRest/ficheros/tiendas.json"

ficheroEmpleados="../tareaApiRest/ficheros/empleados.json"

#creo un objeto blueprint (le doy nombre)
tiendasBP=Blueprint("tiendas", __name__)

#pongo aqui metodo pillar nuevo id porque no va en funciones
#busca siguiente id que asignar a nuevo post de tienda guardando la ultima posicion de la lista (max) y le añade 1
def _find_Next_Id():
    #doy a tiendas el valor devuelto por leer fichero
    tiendas = leerFichero(ficheroTiendas)
    return max(tienda["id"] for tienda in tiendas)+1 

#@cambio @app por @ nombre de objeto BP (tiendasBP)

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el get
@tiendasBP.get("/")
#modifico comportamiento de get con siguiente funcion getTiendas 
def getTiendas():
    #doy a tiendas el valor devuelto por leer fichero
    tiendas=leerFichero(ficheroTiendas)
    #devuelvo el fichero aplicandole jsonify(formato json)
    return jsonify(tiendas)

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el get usando id
#<>indica parametro entrada tipo int llamado id sera el tienda en concreto a mostrar con get
@tiendasBP.get("/<int:id>")
def getTienda(id):
    #doy a tiendas el valor devuelto por leer fichero
    tiendas=leerFichero(ficheroTiendas)
    
    for tienda in tiendas:
        #busco el tienda de id especificado
        if tienda["id"]==id:
            #si lo encuentro hago return de tienda y codigo ok
            return tienda, 200
        
    #de lo contrario devuelvo error no encontrado y codigo no encontrado
    return{"error": "empleado not found"}, 404

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el post
@tiendasBP.post("/")
@jwt_required()
#modifico comportamiento de post con siguiente funcion addTienda 
def addTienda():
    #doy a tiendas el valor devuelto por leer fichero
    tiendas=leerFichero(ficheroTiendas)
    
    #si la peticion es json
    if request.is_json:
        #doy a tienda valor del json de la peticion
        tienda=request.get_json()
        #asigno nueva id con find next id a tienda
        tienda ["id"]=_find_Next_Id()
        # y lo agrego a tiendas
        tiendas.append(tienda)
        
        # escribo el nuevo tiendas en mi fichero
        escribeFichero(ficheroTiendas, tiendas)
    
        #devuelvo tiendas y codigo agregado
        return tienda, 201
    #de lo contrario devuelvo error la peticion debe ser json y codigo debe ser json
    return {"error":"Request must be JSON"}, 415




#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el put usando id
#<>indica parametro entrada tipo int llamado id sera el tienda en concreto a modificar con put
@tiendasBP.put("/<int:id>")
@tiendasBP.patch("/<int:id>")
@jwt_required()
#modifico comportamiento de put con siguiente funcion puttienda 
def modificarTienda(id):
    #doy a tiendas el valor devuelto por leer fichero
    tiendas=leerFichero(ficheroTiendas)
    #si la peticion es json
    if request.is_json:
        #doy a nuevaTienda valor del json de la peticion
        nuevaTienda=request.get_json()
        
        for tienda in tiendas:
             #recorro los tiendas hasta encontrar uno de id igual a la dada
            if tienda ["id"]==id:
                #una vez encontrado el elemento a modificar reemplazo sus valores por los de nuevaTienda
                for clave in nuevaTienda:
                     tienda [clave]=nuevaTienda[clave] 
                    # escribo el nuevo tiendas en mi fichero
                # escribo el nuevo tiendas en mi fichero
                escribeFichero(ficheroTiendas, tiendas)
                #y devuelvo el pais modificado y codigo ok
                return tienda, 200
    #de lo contrario devuelvo error la peticion debe ser json y codigo debe ser json
    return {"Error": "Request must be JSON"}, 415

#debido a la logica de la funcion todo funciona como en el put solo que modifico un dato y no todos del elemento


#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el delete usando id
#<>indica parametro entrada tipo int llamado id sera el tienda en concreto a borrar con deleteTienda
@tiendasBP.delete("/<int:id>")
@jwt_required()
#modifico comportamiento de put con siguiente funcion deleteTienda 
def deleteTienda(id):
    #doy a tiendas el valor devuelto por leer fichero
    tiendas=leerFichero(ficheroTiendas)
    
    #recorro los tiendas hasta encontrar uno de id igual a la dada
    for tienda in tiendas:
        
        #si encuentro el id especificado
        if tienda["id"]==id:
            #una vez encontrado el elemento a modificar borro sus valores  
            tiendas.remove(tienda)
            # escribo el nuevo tiendas en mi fichero
            escribeFichero(ficheroTiendas, tiendas)
            
            #devuelvo diccionario vacio y codigo ok
            return "{}", 200
        
        #de lo contrario devuelvo error no encontrado y codigo no encontrado
        return{"Error": "tienda not found"}, 404
    
    

#get anidado de empleado de una tienda concreta
@tiendasBP.get("/<int:id>/empleados")
def get_empleados(id):
    list = []
    empleados = leerFichero(ficheroEmpleados)
    for empleado in empleados:
        if empleado['idTienda'] == id:
            list.append(empleado)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No empleados for this tienda"}, 404
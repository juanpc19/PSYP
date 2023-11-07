
from utils.funciones import leerFichero, escribeFichero

#necesito blueprint para rutas y funciones y jsonify para formato
from flask import Blueprint, jsonify, request

from flask_jwt_extended import jwt_required

ficheroEmpleados="../tareaApiRest/ficheros/empleados.json"

empleadosBP=Blueprint("empleados", __name__)

#pongo aqui metodo pillar nuevo id porque no va en funciones
#busca siguiente id que asignar a nuevo post de empleado guardando la ultima posicion de la lista (max) y le añade 1
def _find_Next_Id():
    #doy a empleados el valor devuelto por leer fichero
    empleados = leerFichero(ficheroEmpleados)
    return max(empleado["id"] for empleado in empleados)+1 

#@cambio @app por @ nombre de objeto BP (empleadosBP)

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el get
@empleadosBP.get("/")

#modifico comportamiento de get con siguiente funcion getempleados 
def getEmpleados():
    #doy a empleados el valor devuelto por leer fichero
    empleados=leerFichero(ficheroEmpleados)
    #devuelvo el fichero aplicandole jsonify(formato json)
    return jsonify(empleados)

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el get usando id
#<>indica parametro entrada tipo int llamado id sera el empleado en concreto a mostrar con get
@empleadosBP.get("/<int:id>")
def getEmpleado(id):
    #doy a empleados el valor devuelto por leer fichero
    empleados=leerFichero(ficheroEmpleados)
    
    for empleado in empleados:
        #busco el empleado de id especificado
        if empleado["id"]==id:
            #si lo encuentro hago return de empleado y codigo ok
            return empleado, 200
        
    #de lo contrario devuelvo error no encontrado y codigo no encontrado
    return{"error": "empleado not found"}, 404

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el post
@empleadosBP.post("/")
@jwt_required()
#modifico comportamiento de post con siguiente funcion addEmpleado 
def addEmpleado():
    #doy a empleados el valor devuelto por leer fichero
    empleados=leerFichero(ficheroEmpleados)
    
    #si la peticion es json
    if request.is_json:
        #doy a empleado valor del json de la peticion
        empleado=request.get_json()
        #asigno nueva id con find next id a empleado
        empleado ["id"]=_find_Next_Id()
        # y lo agrego a empleados
        empleados.append(empleado)
        
        # escribo el nuevo empleados en mi fichero
        escribeFichero(ficheroEmpleados, empleados)
    
        #devuelvo empleados y codigo agregado
        return empleado, 201
    #de lo contrario devuelvo error la peticion debe ser json y codigo debe ser json
    return {"error":"Request must be JSON"}, 415


#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el put usando id
#<>indica parametro entrada tipo int llamado id sera el empleado en concreto a modificar con put
@empleadosBP.put("/<int:id>")
@empleadosBP.patch("/<int:id>")
@jwt_required()
#modifico comportamiento de put con siguiente funcion putempleado 
def modificarEmpleado(id):
    #doy a empleados el valor devuelto por leer fichero
    empleados=leerFichero(ficheroEmpleados)
    #si la peticion es json
    if request.is_json:
        #doy a nuevoEmpleado valor del json de la peticion
        nuevoEmpleado=request.get_json()
        
        for empleado in empleados:
             #recorro los empleados hasta encontrar uno de id igual a la dada
            if empleado ["id"]==id:
                #una vez encontrado el elemento a modificar reemplazo sus valores por los de nuevoEmpleado
                for clave in nuevoEmpleado:
                     empleado [clave]=nuevoEmpleado[clave] 
                    # escribo el nuevo empleados en mi fichero
                # escribo el nuevo empleados en mi fichero
                escribeFichero(ficheroEmpleados, empleados)
                #y devuelvo el pais modificado y codigo ok
                return empleado, 200
    #de lo contrario devuelvo error la peticion debe ser json y codigo debe ser json
    return {"Error": "Request must be JSON"}, 415

#debido a la logica de la funcion todo funciona como en el put solo que modifico un dato y no todos del elemento

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el delete usando id
#<>indica parametro entrada tipo int llamado id sera el empleado en concreto a borrar con deleteEmpleado
@empleadosBP.delete("/<int:id>")
@jwt_required()
#modifico comportamiento de put con siguiente funcion deleteEmpleado 
def deleteEmpleado(id):
    #doy a empleados el valor devuelto por leer fichero
    empleados=leerFichero(ficheroEmpleados)
    
    #recorro los empleados hasta encontrar uno de id igual a la dada
    for empleado in empleados:
        
        #si encuentro el id especificado
        if empleado["id"]==id:
            #una vez encontrado el elemento a modificar borro sus valores  
            empleados.remove(empleado)
            # escribo el nuevo empleados en mi fichero
            escribeFichero(ficheroEmpleados, empleados)
            
            #devuelvo diccionario vacio y codigo ok
            return "{}", 200
        
        #de lo contrario devuelvo error no encontrado y codigo no encontrado
        return{"Error": "empleado not found"}, 404
    
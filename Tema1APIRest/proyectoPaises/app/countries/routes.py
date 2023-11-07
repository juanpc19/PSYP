
from utils.funciones import leerFichero, escribeFichero

#necesito blueprint para rutas y funciones y jsonify para formato
from flask import Blueprint, jsonify, request

ficheroCountries = "../proyectoPaises/ficheros/countries.json"
ficheroCities = "../proyectoPaises/ficheros/cities.json"

#ficheroCountries = "proyectoPaises\ficheros\countries.json"
#ficheroCities = "proyectoPaises\ficheros\cities.json"

#ficheroCountries = "C:\Users\juanp\OneDrive\Documentos\GitHub\Tema1APIRest\proyectoPaises\ficheros\countries.json"
#ficheroCities = "C:\Users\juanp\OneDrive\Documentos\GitHub\Tema1APIRest\proyectoPaises\ficheros\cities.json"

#creo un objeto blueprint (le doy nombre)
countriesBP=Blueprint("countries", __name__)

#pongo aqui metodo pillar nuevo id porque no va en funciones
#busca siguiente id que asignar a nuevo post de country guardando la ultima posicion de la lista (max) y le añade 1
def _find_Next_Id():
    #doy a countries el valor devuelto por leer fichero
    countries = leerFichero()
    return max(country["id"] for country in countries)+1 

#@cambio @app por @ nombre de objeto BP (countriesBP)

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el get
@countriesBP.get("/")
#modifico comportamiento de get con siguiente funcion getCountries 
def getCountries():
    #doy a countries el valor devuelto por leer fichero
    countries=leerFichero(ficheroCountries)
    #devuelvo el fichero aplicandole jsonify(formato json)
    return jsonify(countries)

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el get usando id
#<>indica parametro entrada tipo int llamado id sera el country en concreto a mostrar con get
@countriesBP.get("/<int:id>")
def getCountry(id):
    #doy a countries el valor devuelto por leer fichero
    countries=leerFichero(ficheroCountries)
    
    for country in countries:
        #busco el country de id especificado
        if country["id"]==id:
            #si lo encuentro hago return de country y codigo ok
            return country, 200
        
    #de lo contrario devuelvo error no encontrado y codigo no encontrado
    return{"error": "country not found"}, 404

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el post
@countriesBP.post("/")
#modifico comportamiento de post con siguiente funcion addCountry 
def addCountry():
    #doy a countries el valor devuelto por leer fichero
    countries=leerFichero(ficheroCountries)
    
    #si la peticion es json
    if request.is_json:
        #doy a country valor del json de la peticion
        country=request.get_json()
        #asigno nueva id con find next id a country
        country ["id"]=_find_Next_Id()
        # y lo agrego a countries
        countries.append(country)
        
        # escribo el nuevo countries en mi fichero
        escribeFichero(ficheroCountries, countries)
    
        #devuelvo countries y codigo agregado
        return country, 201
    #de lo contrario devuelvo error la peticion debe ser json y codigo debe ser json
    return {"error":"Request must be JSON"}, 415

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el put usando id
#<>indica parametro entrada tipo int llamado id sera el country en concreto a modificar con put
@countriesBP.put("/<int:id>")
#modifico comportamiento de put con siguiente funcion putCountry 
def putCountry(id):
    #doy a countries el valor devuelto por leer fichero
    countries=leerFichero(ficheroCountries)
    #si la peticion es json
    if request.is_json:
        #doy a newCountry valor del json de la peticion
        newCountry=request.get_json()
        
        for country in countries:
             #recorro los countries hasta encontrar uno de id igual a la dada
            if country ["id"]==id:
                #una vez encontrado el elemento a modificar reemplazo sus valores por los de newCountry
                for clave in newCountry:
                     country [clave]=newCountry[clave] 
                    # escribo el nuevo countries en mi fichero
                # escribo el nuevo countries en mi fichero
                escribeFichero(ficheroCountries, countries)
                #y devuelvo el pais modificado y codigo ok
                return country, 200
    #de lo contrario devuelvo error la peticion debe ser json y codigo debe ser json
    return {"Error": "Request must be JSON"}, 415

#como patch hace lo mismo que put (gracias al funcionamiento del 2º bucle for que recorre el json newCountry sustituyendo valores)
# podria poner la etiqueta patch justo debajo de put y ahorrarme codigo, asi al usar el modulo patch.py desde la terminal 
# ejecutaria el codigo de dentro de putCountry con el dato del diccionario del modulo patch.py

#debido a la logica de la funcion todo funciona como en el put solo que modifico un dato y no todos del elemento
@countriesBP.patch("/<int:id>")
def patchCountry(id):
    if request.is_json:
        newCountry=request.get_json()
        countries=leerFichero(ficheroCountries)
        
        for country in countries:
            if country ["id"]==id:
                for clave in newCountry:
                     country [clave]=newCountry[clave]  
                # escribo el nuevo countries en mi fichero
                escribeFichero(ficheroCountries, countries)   
                return country, 200
    
    return {"Error": "Request must be JSON"}, 415

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el delete usando id
#<>indica parametro entrada tipo int llamado id sera el country en concreto a borrar con deletePost
@countriesBP.delete("/<int:id>")
#modifico comportamiento de put con siguiente funcion deletePost 
def deletePost(id):
    #doy a countries el valor devuelto por leer fichero
    countries=leerFichero()
    
    #recorro los countries hasta encontrar uno de id igual a la dada
    for country in countries:
        
        #si encuentro el id especificado
        if country["id"]==id:
            #una vez encontrado el elemento a modificar borro sus valores  
            countries.remove(country)
            # escribo el nuevo countries en mi fichero
            escribeFichero(ficheroCountries, countries)
            
            #devuelvo diccionario vacio y codigo ok
            return "{}", 200
        
        #de lo contrario devuelvo error no encontrado y codigo no encontrado
        return{"Error": "Country not found"}, 404
    
    
#no se para que este get aqui
@countriesBP.get("/<int:id>/cities")
def get_cities(id):
    list = []
    cities = leerFichero(ficheroCities)
    for city in cities:
        if city['countryId'] == id:
            list.append(city)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No cities for this country"}, 404
from flask import*

#instancio una aplicacion flask usada para manejar solicitudes web y definir rutas, vistas y comportamientos especificos de la aplicacion
# __name__ variable especial en python se refiere al nombre del modulo donde esta el codigo
app=Flask(__name__)
    
#declaro variable donde guardo nombre fichero (sirve como ruta para encontrarlo al estar este en misma carpeta)
nombreFichero = "countries.json"

#funcion que guarda abre nombreFichero en modo lectura guardando esta lectura en archivo lo cual me permite leer o modificar el archivo desde python, 
# carga el objeto creado (archivo) en countries en formato json,
# cierra el archivo y devuelve el contenido del mismo que ahora esta en countries en el return
def leerFichero():
    archivo = open(nombreFichero, "r") 
    countries = json.load(archivo)
    archivo.close()
    return countries

#funcion que recibe un diccionario abre nombreFichero en modo escritura guardando esta escritura en archivo lo cual me permite leer o modificar el archivo desde python,
# sobreescribe el objeto creado (archivo) con los valores de countries (el diccionario con valor/valores de turno) y cierra el archivo
def escribeFichero(countries):
    archivo = open(nombreFichero, "w")
    json.dump(countries,archivo)
    archivo.close()

#busca siguiente id que asignar a nuevo post de country guardando la ultima posicion de la lista (max) y le añade 1
def _find_Next_Id():
    #doy a countries el valor devuelto por leer fichero
    countries = leerFichero()
    return max(country["id"] for country in countries)+1 

#defino ruta raiz o index
@app.route("/")
#lo que muestro al acceder a index (menu, se puede llamar diferente), puede ser html en lugar de simple string
def index():
    return'Hola a todos :)'

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el get
@app.get("/countries")
#modifico comportamiento de get con siguiente funcion getCountries 
def getCountries():
    #doy a countries el valor devuelto por leer fichero
    countries=leerFichero()
    #devuelvo el fichero aplicandole jsonify(formato json)
    return jsonify(countries)

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el get usando id
#<>indica parametro entrada tipo int llamado id sera el country en concreto a mostrar con get
@app.get("/countries/<int:id>")
def getCountry(id):
    #doy a countries el valor devuelto por leer fichero
    countries=leerFichero()
    
    for country in countries:
        #busco el country de id especificado
        if country["id"]==id:
            #si lo encuentro hago return de country y codigo ok
            return country, 200
        
    #de lo contrario devuelvo error no encontrado y codigo no encontrado
    return{"error": "country not found"}, 404

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el post
@app.post("/countries")
#modifico comportamiento de post con siguiente funcion addCountry 
def addCountry():
    #doy a countries el valor devuelto por leer fichero
    countries=leerFichero()
    
    #si la peticion es json
    if request.is_json:
        #doy a country valor del json de la peticion
        country=request.get_json()
        #asigno nueva id con find next id a country
        country ["id"]=_find_Next_Id()
        # y lo agrego a countries
        countries.append(country)
        # escribo el nuevo countries en mi fichero
        escribeFichero(countries)
    
        #devuelvo countries y codigo agregado
        return country, 201
    #de lo contrario devuelvo error la peticion debe ser json y codigo debe ser json
    return {"error":"Request must be JSON"}, 415

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el put usando id
#<>indica parametro entrada tipo int llamado id sera el country en concreto a modificar con put
@app.put("/countries/<int:id>")
#modifico comportamiento de put con siguiente funcion putCountry 
def putCountry(id):
    #doy a countries el valor devuelto por leer fichero
    countries=leerFichero()
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
                escribeFichero(countries) 
                #y devuelvo el pais modificado y codigo ok
                return country, 200
    #de lo contrario devuelvo error la peticion debe ser json y codigo debe ser json
    return {"Error": "Request must be JSON"}, 415

#como patch hace lo mismo que put (gracias al funcionamiento del 2º bucle for que recorre el json newCountry sustituyendo valores)
# podria poner la etiqueta patch justo debajo de put y ahorrarme codigo, asi al usar el modulo patch.py desde la terminal 
# ejecutaria el codigo de dentro de putCountry con el dato del diccionario del modulo patch.py

#debido a la logica de la funcion todo funciona como en el put solo que modifico un dato y no todos del elemento
@app.patch("/countries/<int:id>")
def patchCountry(id):
    if request.is_json:
        newCountry=request.get_json()
        countries=leerFichero()
        
        for country in countries:
            if country ["id"]==id:
                for clave in newCountry:
                     country [clave]=newCountry[clave]  
                # escribo el nuevo countries en mi fichero
                escribeFichero(countries)     
                return country, 200
    
    return {"Error": "Request must be JSON"}, 415

#hago referencia a objeto tipo flask usando decorador para indicar que voy a modificar el comportamiento del metodo asociado 
#especifico ruta donde se efectuara el delete usando id
#<>indica parametro entrada tipo int llamado id sera el country en concreto a borrar con deletePost
@app.delete("/countries/<int:id>")
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
            escribeFichero(countries) 
            
            #devuelvo diccionario vacio y codigo ok
            return "{}", 200
        
        #de lo contrario devuelvo error no encontrado y codigo no encontrado
        return{"Error": "Country not found"}, 404


#si cumple es fichero main y ejecuta el main, esto debe estar al final del archivo no se porque
if __name__=="__main__":
    #debug modo desarrollo on/true, host por defecto, port el que quieras
    app.run(debug=True, host="0.0.0.0", port=5050)
    
# instalar flask en cdm con py -m pip install flask
# al hacer por cmd dir para ver directorios desde aqui igual en terminal vs, 
# ponerme en carpeta servidor con cd ruta entera servidor,
# py app.py en terminal power shell para encender el servidor
# en otro terminal power shell hacer py post.py para hacer un post (o cualquiera otra cosa)


#request para peticiones nivel servidor
#flask para peticiones y modificar comportamiento servidor frente a peticiones respecto a estas nivel servidor


#ANIDAMIENTOS:
#countries tiene cities 
#country(id,name)
#city(id,name,idCountry)

#definiremos una estructura de carpetas y ficheros donde tenerlo todo ordenado.
#Utilizaremos un elemento de Flask llamado Blueprint que nos permite dividir una aplicación Flask en distintos módulos.

#cada carpeta necesita tener __init__.py para poder importar paquete (carpeta?)
#dentro de route definir get post y tal con endpoint(rutas url)

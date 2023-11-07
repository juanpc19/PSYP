
from app import app

#si cumple es fichero main y ejecuta el main, esto debe estar al final del archivo no se porque
if __name__== "__main__":
    #debug modo desarrollo on/true, host por defecto, port el que quieras
    app.run(debug=True, host="0.0.0.0", port=5050)
    
    
    
# instalar flask en cdm con py -m pip install flask
# al hacer por cmd dir para ver directorios desde aqui igual en terminal vs, 
# ponerme en carpeta con el run con cd,
# py app.py en terminal power shell para encender el servidor
# en otro terminal power shell hacer py post.py para hacer un post (o cualquiera otra cosa, cd si hace falta)


#request para peticiones a nivel servidor
#flask para peticiones y modificar comportamiento servidor frente a peticiones respecto a estas, nivel servidor
#blueprint para anidamientos
#Utilizaremos un elemento de Flask llamado Blueprint que nos permite dividir una aplicación Flask en distintos módulos.


#ANIDAMIENTOS:
#countries tiene cities 
#country(id,name)
#city(id,name,idCountry)


#cada carpeta necesita tener __init__.py para poder importar paquete (carpeta?)
#dentro de route definir get post y tal con endpoint(rutas url), comportamiento app 

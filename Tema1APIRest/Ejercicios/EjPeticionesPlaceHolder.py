#importo todo del modulo Funciones
from Funciones import *

#guardo la url a usar
url="https://jsonplaceholder.typicode.com/posts"

#guardo opcion seleccionada por usuario
opcion=1
diccionario={}
userId=0
id=0
title=""
body=""
datoModificar=""


while opcion!=0:
    
    print("""
          1. Mostrar las publicaciones.
          2. Mostrar una publicacion concreta.
          3. Añadir una nueva publicacion.
          4. Modificar todos los datos de una publicacion.
          5. Modificar un dato concreto de una publicacion.
          6. Eliminar una publicacion.
          0. Salir de la aplicacion.
          """)
    
    opcion=int(input()) 
        # llamo a funcion get all posts y le paso url
    if opcion==1:
        getAllPosts(url)
        
    elif opcion==2:
        
        #recojo dato identificador de post, BUSCARA POR ID NO POR USER ID
        numP=(input("Introduzca numero de publicacion:"))
        # llamo a funcion get post y le paso url y diccionario 
        getPost(url, numP)
        
    #creo nuevo post en servidor
    elif opcion==3:
        #recojo datos de post, modificar para input manual custom con variables 
        diccionario={'userId': 10, 'id': 101, 'title': 'añado primera cosa','body': 'siuuuuuuuuuuuuuuu'}
        # llamo a funcion añade post y le paso url y diccionario 
        addPost(url, diccionario)
        
    #reemplazo/creo post en servidor
    elif opcion==4:
        
        #solicito datos a usuario
        userId=input("Introduzca el userId:")
        id=input("Introduzca el id del post a modificar:")
        title=input(str("Introduzca el title:"))
        body=input (str("Introduzca el body:"))
        #guardo datos en diccionario
        diccionario={'userId': userId, 'id': id, 'title': title,'body': body}
        
        #llamo a funicon putPost y le paso url, diccionario y id
        putPost(url, diccionario, id)
    
    #reemplazo parcialmente un post
    elif opcion==5:
        #solicito id del post a modificar
        id=input("Introduzca el id del post a modificar:")
        #solicito al usuario campo a modificar
        datoModificar=input("Indique que dato desea modificar (userId,title,body):")
        
        #si el campo es userId
        if datoModificar=="userId":
            #solicito valor
            userId=input("Introduzca el userId:")
            #añado valor a diccionario
            diccionario={'userId': userId}
            #llamo a funicon patchPost y le paso url, diccionario y id
            patchPost(url, id, diccionario)
        
        #si el campo es title
        elif datoModificar=="title":
            #solicito valor
            title=input(str("Introduzca el title:"))
            #añado valor a diccionario
            diccionario={'title': title}
            #llamo a funicon patchPost y le paso url, diccionario y id
            patchPost(url, id, diccionario)
        
        #si el campo es body    
        elif datoModificar=="body":
            #solicito valor
            body=input(str("Introduzca el body:"))
            #añado valor a diccionario
            diccionario={'body': body}
            #llamo a funicon patchPost y le paso url, diccionario y id
            patchPost(url, id, diccionario)
       
    elif opcion==6:
        #solicito id a usuario
        id=input("Introduzca el id del post a modificar:")
        
        #llamo a funicon deletePost y le paso url y id
        deletePost(url, id)
          
      
        
            
        
    
    
#importo requests de .venv(virtualenviroment) he de crear uno con shift+ctrl+p, en tipo seleccionar vevn y en interprete el que desee o este usando
import requests
   
    #metodo para hacer get de todos los post
def getAllPosts(url):
    #guardare la respuesta de la peticion get a la url en response
    response=requests.get(url)
    
    #si la respuesta da codigo 200 (ok)
    if response.status_code==200:
        #guardo en lista la respuesta en formato json
        lista=response.json()
        #procedo a recorrer los elementos tipo diccionario guardados en lista
        for diccionario in lista:
            #a su vez recorro cada dicciconario haciendo print de su clave y valor
            for clave in diccionario:
                print(clave, ":", diccionario[clave])
                print()
                
    else:
        #si el codigo devuelto por response no es 200 comunico error de peticion con print
         print("La peticion no ha terminado correctamente, codigo:", response.status_code)
                
            
    #metodo para hacer get de un post en concreto
def getPost(url, numP):
    #guardare la respuesta de la peticion get de un recurso en concreto a la url en response
    response=requests.get(url+"/"+str(numP))
    
    #si la respuesta da codigo 200 (ok)
    #hago print del elemento en formato json
    if response.status_code==200:
        print(response.json())
        
    #si el codigo devuelto por response no es 200 comunico error de peticion con print       
    else:print("La peticion no ha terminado correctamente, codigo:", response.status_code)
    
    #metodo para añadir post
def addPost(url, diccionario):
    #guardare la respuesta de la peticion post a la url en response
    response=requests.post(url, json=diccionario)
    
    #si la respuesta da codigo 201 (creado)
    if response.status_code==201:
        #comunico creacion exitosa de post con mensaje
        print("Se ha creado el siguiente post correctamente:")
        print(response.json())
        
    #si el codigo devuelto por response no es 201 comunico error de peticion con print    
    else:print("La peticion no ha terminado correctamente, codigo:", response.status_code)
    
    
    #metodo para reemplazar o añadir post
def putPost(url, diccionario, id):
    #modifico la url usando la id
    url+="/"+id
    #2 lineas siguientes para comprobar cambio con get
    response=requests.get(url)
    print(response.json())
    
    #guardare la respuesta de la peticion put de un recurso en concreto a la url en response
    response=requests.put(url,json=diccionario)
    
    #si la respuesta da codigo 200 (ok)
    #hago print del elemento en formato json
    if response.status_code==200:
        print("Se ha reemplazado/creado el siguiente post correctamente")
        print(response.json())
    
    #si el codigo devuelto por response no es 201 comunico error de peticion con print 
    else:print("La peticion no ha terminado correctamente, codigo:", response.status_code)
    
    #metodo para modificar parcialmente post
def patchPost(url, id, diccionario):
    #modifico la url usando la id
    url+="/"+id
    #2 lineas siguientes para comprobar cambio con get
    response=requests.get(url)
    print(response.json())
    
    #guardare la respuesta de la peticion put de un recurso en concreto a la url en response
    response=requests.patch(url,json=diccionario)
    
    #si la respuesta da codigo 200 (ok)
    #hago print del elemento en formato json
    if response.status_code==200:
        print("Se ha modificado parcialmente el siguiente post correctamente")
        print(response.json())
    
    #si el codigo devuelto por response no es 201 comunico error de peticion con print 
    else:print("La peticion no ha terminado correctamente, codigo:", response.status_code)

    #metodo para borrar post
def deletePost(url, id):
    #modifico la url usando la id
    url+="/"+id
    #2 lineas siguientes para comprobar cambio con get
    response=requests.get(url)
    print(response.json())
    
    #guardare la respuesta de la peticion put de un recurso en concreto a la url en response
    response=requests.delete(url)
    
    #si la respuesta da codigo 200 (ok)
    #hago print del elemento en formato json
    if response.status_code==200:
        print("Se ha borrado el siguiente post correctamente")
        print(response.json())
    
    #si el codigo devuelto por response no es 201 comunico error de peticion con print 
    else:print("La peticion no ha terminado correctamente, codigo:", response.status_code)
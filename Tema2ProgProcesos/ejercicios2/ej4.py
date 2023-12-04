from multiprocessing import Queue,Process

#proceso 1 filtra por año y pasa pelicula proceso 2 por cola
def filtraPeliculas(cola,rutafichero, year):
    try:
        with open(rutafichero, "r") as listaPeliculas:
            cola.put(year) #mando año por cola
            
            for linea in listaPeliculas.readlines():
                #split para recoger año
                pelicula=linea.split(";")
                #si año pelicula igual a año param entrada
                if int(pelicula[1])==year:
                    #la añado a la cola
                    cola.put(linea)
            #si no ha mas peliculas añado none a cola
            cola.put(None)  
              
    except FileNotFoundError:   
        print("Archivo no encontrado.")
    except Exception as e:
        print("El siguiente error ha ocurridoa:", e)
                    

#recibe pelicula y año de cola y la escribe en fichero con nombre pelicula+año
def listaPeliculas(cola):
    year=cola.get() #recibo año por cola
    plantillaFichero = f"Tema2ProgProcesos\\ejercicios\\ficheros\\ej4\\peliculas{year}.txt" #añado año y .txt
    
    try:
        with open(plantillaFichero, "a") as listaPeliculas:
            #recojo pelicula de cola
            pelicula=cola.get()
            #bucle se ejecutara has que pelicula sea none (fin de cola)
            while pelicula is not None:
                #escribo pelicula
                listaPeliculas.write(pelicula+"\n")
                #recojo siguiente de la cola
                pelicula=cola.get()
                
                
    except FileNotFoundError:   
        print("Archivo no encontrado.")
    except Exception as e:  
        print("El siguiente error ha ocurrido:", e)

if __name__=="__main__":
    #siguiente linea ruta hasta carpeta con peliculas.txt
    #"Tema2ProgProcesos\\ejercicios\\ficheros\\ej4\\peliculas.txt"
    
    rutafichero=input("Introduzca ruta de fichero que contiene las peliculas: ")
    year=int(input("Introduzca año por el que filtrar: "))
    
    cola=Queue()
    
    p1=Process(target=filtraPeliculas, args=(cola,rutafichero,year))
    p2=Process(target=listaPeliculas, args=(cola,))
    
    p1.start()
    p2.start()
    
    #no parece haber necesidad de join?
    
   
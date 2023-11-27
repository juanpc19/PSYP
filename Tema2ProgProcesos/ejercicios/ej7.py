from asyncio import Queue
from multiprocessing import Pool, Process
import os
import time

#productor
def leerFicheroCola(cola):
    listaNumeros = []
    try:
        #apertura archivo con autocierre requiere indentacion sig linea
        with open("ficheros/2numeros.txt", 'rt') as f:
            #recorro archivo leyendo todas las lineas
            for linea in f.readlines():
                #las voy añadiendo a cola quitandoles el salto de lina con strip
                numeros = linea.strip().split()
                listaNumeros.append([int(number) for number in listaNumeros])
                cola.put(listaNumeros)
            #si no hay mas elementos que añadir a la cola añado None para indicar a proceso final de cola
            cola.put(None)
                
    except FileNotFoundError:   
        print("Archivo no encontrado.")
    except Exception as e:
        print("El siguiente error ha ocurrido:", e)
        
        
def sumatorioCola(cola):
    #cojo primer item de la cola
    itemCola=cola.get()
    #bucle se ejecuta mientras haya items en cola diferente a none
    while itemCola is not None:
        sumados=0
        #hago sumatorio del itemCola actual con bucle for
        for i in range(1,itemCola+1):
            sumados+=i
        #muestro resultado sumatorio en print (no se hacer return de varios sumatorios, guardar en lista resultados?))
        print(sumados)
        #cojo siguiente item en cola y repito todo hasta que no queden items en cola o este ultimo sea none
        itemCola=cola.get()
        
       
if __name__=="__main__":
    #terminal hecho codigo, me pone en la siguiente localizacion como usando cd, pero lo hace auto al ejecutar programa
    directorio = "Tema2ProgProcesos/ejercicios" #ruta absoluta en la que me pondra el programa al ejecutar
    # cambia el directorio usado actual
    os.chdir(directorio)
    # muestra el directorio usado actual
    print("Directorio actual:", os.getcwd())
    
      #creo coleccion tipo Queue
    cola=Queue()
    
    #creo procesos y les paso como argumento la coleccion en forma de una tupla
    p1=Process(target=leerFicheroCola, args=(cola,))
    p2=Process(target=sumatorioCola, args=(cola,))
    
    #inicio procesos y dejo que se ejecuten a su ritmo default
    p1.start()
    p2.start()
from multiprocessing import Process,Pipe
import os
import time
        
#productor
def leerFichero(extremo):
   
    try:
        #apertura archivo con autocierre requiere indentacion sig linea
        with open("ficheros/numeros.txt", 'rt') as f:
            #recorro archivo leyendo todas las lineas
            for linea in f.readlines():
                #las voy enviando por pipe quitandoles el salto de lina con strip
                lineaInt=int(linea.strip())
                extremo.send(lineaInt)
            #si no hay mas elementos que enviar paso None para indicar a proceso final de envio de datos
            extremo.send(None)
            extremo.close()
                
    except FileNotFoundError:   
        print("Archivo no encontrado.")
    except Exception as e:
        print("El siguiente error ha ocurrido:", e)

#consumidor
def sumatorio(extremo):
    #recibo datos de extremo de pipe
    datoRecibido=extremo.recv()
    #bucle se ejecuta mientras reciba datos diferentes a none
    while datoRecibido is not None:
        sumados=0
        #hago sumatorio del datoRecibido actual con bucle for
        for i in range(1,datoRecibido+1):
            sumados+=i
        #muestro resultado sumatorio en print (no se hacer return de varios sumatorios, guardar en lista resultados?))
        print(sumados)
        #cojo siguiente datoRecibido y repito todo hasta que no reciba datoRecibido o este ultimo sea none
        datoRecibido=extremo.recv()
    extremo.close()
    
if __name__ == "__main__":
    #terminal hecho codigo, me pone en la siguiente localizacion como usando cd, pero lo hace auto al ejecutar programa
    directorio = "Tema2ProgProcesos/ejercicios" #ruta absoluta en la que me pondra el programa al ejecutar
    # cambia el directorio usado actual
    os.chdir(directorio)
    # muestra el directorio usado actual
    print("Directorio actual:", os.getcwd())
    
    #creo coleccion tipo Queue
    izq, der = Pipe()
    
    #creo procesos y les paso como argumento la coleccion en forma de una tupla
    p1=Process(target=leerFichero, args= (izq,))
    p2=Process(target=sumatorio, args= (der,))
    
    #inicio procesos y dejo que se ejecuten a su ritmo default
    p1.start()
    p2.start()
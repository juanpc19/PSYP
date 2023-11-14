from multiprocessing import Process
import time

#funcion que devuelve sumatorio de 2 numeros dados como param entrada
def sumatorio(numero1,numero2):
    # si numero 2 menor que numero 1 intercambio valores para que for funcione
    if numero2<numero1:
        numero1,numero2=numero2,numero1
    #si ambos numeros son igual o mayor a 1
    if numero1>=1 and numero2>=1:
        sumados=0
        #recorro el rango sumando de numero1 a numero 2 incluido
        for i in range(numero1,numero2+1):
            sumados+=i
        #y hago print de sumados por terminal
        print (sumados)
    else:
        print ("Error introduzca numero igual o mayor a 1.")
        
        
#proceso main
if __name__=="__main__":
    #registro tiempo de inicio
    inicio=time.time()
    
    #creo procesos
    p1=Process(target=sumatorio, args=(5,1))
    p2=Process(target=sumatorio, args=(1,1))
    p3=Process(target=sumatorio, args=(1,6))
    
    # los inicio
    p1.start()
    p2.start()
    p3.start()
    
    # le indico al proceso main que espere a la finalizacion de los procesos p1, p2 y p3
    p1.join()
    p2.join()
    p3.join()
    
    #print de proceso main de finalizacion de proceso
    print ("Todos los procesos han terminado.")
    
    #registro tiempo de finalizacion
    fin=time.time()
    
    # print de timpo ejecucion obtenido de restar x-0
    print ("Tiempo", fin-inicio)
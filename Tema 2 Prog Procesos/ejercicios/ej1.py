from multiprocessing import Process
import time

def sumatorio(numero):
    if numero>=1:
        sumados=0
        for i in range(1,numero+1):
            sumados+=i
        print (sumados)
    else:
        print ("Error introduzca numero igual o mayor a 1.")
        
if __name__=="__main__":
    
    inicio=time.time()
    
    p1=Process(target=sumatorio, args=(5,))
    p2=Process(target=sumatorio, args=(3,))
    p3=Process(target=sumatorio, args=(6,))
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()
    
    print ("Todos los procesos han terminado.")
    
    fin=time.time()
    
    print ("Tiempo", fin-inicio)


from threading import Barrier
from carrera import Carrera


if __name__=="__main__":
    
    barrera=Barrier(10)
    hilos=[]
    
    for i in range (10):
        hilo=Carrera(str(i),barrera)
        hilo.start()
        hilos.append(hilo)
        
    for h in hilos:
        h.join()
        
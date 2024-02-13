
from threading import Barrier, Event, Timer
import time
from pasoPeatones import PasoPeatones

 
if __name__=="__main__":
    
    
    #deberia tener muchos hilos porque 10 peatones no van a volver a pasar por el mismo semaforo
    #cada uno pasa una vez y se va, esto permite que nuevos hilos entren a barrera y cuando salgan no tengan k volver a entrar
    #al romperse la barrera puedo liberar los hilos que esten haciendo wait y al repararla 
    
    #timer en main cambia el estado de evento compartido por hilos
    
    barrera=Barrier(100)
    evento=Event()
    evento.clear()
   
    hilos=[]
    
    for i in range(10):
        
        hilo=PasoPeatones(str(i), barrera, evento)
        hilo.start()
        hilos.append(hilo)
         
        
    for h in hilos:
        h.join()
            
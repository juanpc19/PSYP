from threading import Barrier, Condition, Event
from escapeRoom import EscapeRoom

if __name__=="__main__":
     
    barrera=Barrier(5)
    cond=Condition()
    
    hilos=[]
    
    for i in range (5):
        hilo=EscapeRoom(str(i), barrera, cond)
        hilo.start()
        hilos.append(hilo)
        
        
    for h in hilos:
        h.join()
        
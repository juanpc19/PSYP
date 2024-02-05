from threading import Event

from ratonEvento import Raton


if __name__=="__main__":
    evento = Event()
    evento.set()
    
    hilos =[]
    
    
    for i in range (5):
        hilo=Raton(str(i),evento)
        hilo.start()
        hilos.append(hilo)
        
        
    for h in hilos:
        h.join()
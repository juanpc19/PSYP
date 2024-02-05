from threading import Event

from ratonEvento import Raton


if __name__=="__main__":
    evento = Event()#creo evento
    evento.set()#lo pongo a true
    
    hilos =[]
    
    for i in range (5):
        hilo=Raton(str(i),evento)#le paso el nombre y el evento seteado para k los hilos no esten esperando al empezar
        hilo.start()
        hilos.append(hilo)
        
        
    for h in hilos:
        h.join()
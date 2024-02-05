
from threading import Event
from  numeroOcultoEvento import NumeroOcultoEvento


if __name__=="__main__":
    evento=Event()
    evento.clear()
    
    hilos=[]
    
    for i in range (10):
        hilo=NumeroOcultoEvento(str(i),evento)
        hilo.start()
  
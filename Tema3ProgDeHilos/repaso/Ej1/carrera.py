
from threading import Barrier, Thread


class Carrera (Thread):
    
    def __init__(self, nombre,barrera=Barrier):
        Thread.__init__(self, name=nombre, barrera=barrera)
        
        
    def run (self):
        pass
    #barrera espera 10 hilos, una vez estan todos los lanza tras un delay de 3 seg, aqui calcular tiempo en llgar cada uno (deberia ponerles un delay de varios segundos)
    
    
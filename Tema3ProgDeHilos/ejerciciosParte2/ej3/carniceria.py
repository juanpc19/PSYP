import random
from threading import Semaphore, Thread
import time

class Carniceria(Thread):
    
    semaforo=Semaphore(4)#permite 4 hilos en activo
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run(self):
        print("el cliente ", self.name, "esta dentro de la carniceria")
        Carniceria.semaforo.acquire()
        print("el cliente ", self.name, "esta siendo atendido")
        time.sleep(random.randint(1,11))
        print("el cliente ", self.name, "el cliente ha terminado en la carniceria")
        Carniceria.semaforo.release()

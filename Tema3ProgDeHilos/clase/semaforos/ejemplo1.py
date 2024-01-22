import random
from threading import Semaphore, Thread
import time

class Cajero(Thread):
    
    semaforo=Semaphore(4)
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run (self):
        print("el hilo ", self.name, "esta comprando")
        Cajero.semaforo.acquire()
        print("el hilo ", self.name, "esta en caja")
        time.sleep(random.randint(1,11))
        print("el hilo ", self.name, "ya ha pagado")
        Cajero.semaforo.release()

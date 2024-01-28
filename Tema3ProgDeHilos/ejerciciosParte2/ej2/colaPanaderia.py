import random
from threading import Semaphore, Thread
import time


class ColaPanaderia(Thread):
    
    semaforo=Semaphore(1) #en ej 3 permitir 4 aqui en lugar de 1 que permite un hilo en activo
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run (self):
        print("el cliente ", self.name, "esta esperando a ser atendido")
        ColaPanaderia.semaforo.acquire()
        time.sleep(random.randint(1,6))
        print("el cliente ", self.name, "el cliente ha sido atendido")
        ColaPanaderia.semaforo.release()
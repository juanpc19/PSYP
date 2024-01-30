
import random
from threading import Thread
import time

class Consumidor(Thread):
    def __init__(self, nombre, cola, cond):
        Thread.__init__(self, name=nombre)
        self.cola = cola
        self.cond = cond

    def run(self):
        while True:
            with self.cond:#con condition recibido auto acquire
                while self.cola.empty():#mientras la cola este vacia
                    print("Cola vacía")
                    self.cond.wait()#se bloquea el hilo
                cadena = self.cola.get()#cuando la cola no este vacia se coge cadena de cola
            print("Hilo", self.name, "está recogiendo el objeto...")#se comunica por pantalla con delay
            time.sleep(random.randint(1,5))
            print("Objeto recogido por", self.name, ":", cadena)
            with self.cond:#con condition recibido notificacion a todos los hilos y auto release 
                self.cond.notifyAll()
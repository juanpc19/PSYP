
import random
from threading import Thread
import time
 
class Productor(Thread):
    def __init__(self, nombre, cola, cond):
        Thread.__init__(self, name=nombre)
        self.cola = cola
        self.cond = cond

    def run(self):
        while True:
            cadena = "objeto"
            with self.cond:#con condition recibido auto acquire
                while self.cola.full():#si la cola esta llena (1)
                    print("Cola llena")
                    self.cond.wait()#se bloquea el hilo
                self.cola.put(cadena)# al salir de bucle (si cola no llena) se pone la cadena en la cola
            print("Hilo", self.name, "produciendo...")#se indica por pantalla con delay
            time.sleep(random.randint(1,5))
            print("Hilo", self.name, "termina de producir")
            with self.cond:#con condition recibido notificacion a todos los hilos y auto release 
                self.cond.notifyAll()
        
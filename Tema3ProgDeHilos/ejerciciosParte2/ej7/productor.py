
import random
from threading import Thread
import time
from ej7.main import *



class Productor(Thread):
      
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run(self):
        
        while True:
            cadena="objeto"
            with cond.full():
                while cola.full():
                    print("cola llena")
                    cond.wait()
                cola.put(cadena)
            print("hilo", self.name, "produciendo...")
            time.sleep(random.radint(1,5))
            print("hilo", self.name, "termina de producir")
            cond.notiyAll()

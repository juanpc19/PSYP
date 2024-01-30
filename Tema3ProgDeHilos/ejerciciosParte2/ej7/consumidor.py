
import random
from threading import Thread
import time
from ej7.main import *


class Consumidor(Thread):
      
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run(self):
        
      
        while True:
            with cond:
                while cola.empty():
                    print("coala vacia")
                    cond.wait()
                cadena = cola.get()
                
            print("se esta recogiendo el objeto ", cadena)
            time.sleep(random.randint(1,5))
            print("objeto recogido por ", self.name, cadena)
            cond.notify_all()
     

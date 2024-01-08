import random
from threading import Thread
import time


class HilosTrabajadores(Thread):
    def __init__(self,nombre):
        Thread.__init__(self)
        self.nombre=nombre
        
    def run(self):
        while True:
            print("soy : ", self.nombre, "y estoy trabajando")
            time.sleep(random.uniform(1,10))
            print("soy : ", self.nombre, "y he terminado de trabajar")
            
        
        
        
        
        
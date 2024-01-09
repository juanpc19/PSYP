import random
from threading import Thread
import time


class HilosTrabajadores(Thread):
    def __init__(self,nombre):
        Thread.__init__(self, name=nombre)
        #self.nombre=nombre
        
    def run(self):
        while True:
            print("soy : ", self.getName(), "y estoy trabajando")
            time.sleep(random.uniform(1,10))
            print("soy : ", self.name, "y he terminado de trabajar")
            
            #name=nombre name es propiedad por defecto
            #puedo usar .nombre poco correcto .name correcto o .getName() este ultimo puede dar problemas
            
        
        
        
        
        
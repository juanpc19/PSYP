
import random
from threading import Barrier, Condition, Event, Thread, Timer
import time



class Carrera(Thread):
    
    def __init__(self, nombre, barrera=Barrier, cond=Condition, cond2=Condition):
        Thread.__init__(self, name=nombre)
        self.barrera = barrera
        self.cond=cond
        self.cond2=cond2
        
        
    def run(self):
        print("Hilo", self.name, "en posicion, esperando resto de hilos")
        self.barrera.wait()
        
        
        
        
        
        
        
      
import random
from threading import Semaphore, Thread
import time

class CarniceriaCharcuteria(Thread):
    
    carniceria=Semaphore(4)#permite 4 hilos en activo
    charcuteria=Semaphore(2)
    
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run(self):
        carniceria=False
        charcuteria=False
    
        while not carniceria or not charcuteria:
            if CarniceriaCharcuteria.carniceria._value>0 and not carniceria:
                print("el cliente ", self.name, "ha llegado")
                CarniceriaCharcuteria.carniceria.acquire()
                print("el cliente ", self.name, "esta siendo atendido en carniceria")
                time.sleep(random.randint(1,6))
                print("el cliente ", self.name, "ha terminado en la carniceria")
                CarniceriaCharcuteria.carniceria.release()
            
            if CarniceriaCharcuteria.charcuteria._value>0 and not charcuteria:
                with CarniceriaCharcuteria.charcuteria:
                    charcuteria=True
                    print("el cliente ", self.name, "esta siendo atendido en Charcuteria")
                    time.sleep(random.randint(1,6))
                    print("el cliente ", self.name, "ha terminado en la Charcuteria")
                    
            

import random
from threading import Semaphore, Thread
import time

class CarniceriaCharcuteria(Thread):
    
    carniceria=Semaphore(4)#permite 4 hilos en activo
    charcuteria=Semaphore(2)#permite 2 hilos en activo
    
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run(self):
        carniceriaH=False#determinan si hilo ha acabado en la seccion
        charcuteriaH=False
    
        print("Llega el cliente", self.name)
        
        #mientras el hilo tenga una de las 2 secciones a false continua el bucle
        while not carniceriaH or not charcuteriaH:
            #si carniceriaH es false y el valor de semaforo mayor a 0 (tiene hueco) el hilo hace lock con acquire 
            #(clase.su semaforo._value para valor de semaforo)
            if CarniceriaCharcuteria.carniceria._value>0 and not carniceriaH:
                CarniceriaCharcuteria.carniceria.acquire()
                print("el cliente ", self.name, "esta siendo atendido en carniceria")
                time.sleep(random.randint(1,6))
                print("el cliente ", self.name, "ha terminado en la carniceria")
                carniceriaH=True#el hilo acaba con carniceria
                CarniceriaCharcuteria.carniceria.release()
            
            #si charcuteriaH es false y el valor de semaforo mayor a 0 (tiene hueco) el hilo hace lock con with 
            # (clase.su semaforo para lock auto) (clase.su semaforo._value para valor de semaforo)
            if CarniceriaCharcuteria.charcuteria._value>0 and not charcuteriaH:
                with CarniceriaCharcuteria.charcuteria:
                    print("el cliente ", self.name, "esta siendo atendido en Charcuteria")
                    time.sleep(random.randint(1,6))
                    print("el cliente ", self.name, "ha terminado en la Charcuteria")
                    charcuteriaH=True#el hilo acaba con charcuteria
                    
        print("El cliente", self.name, "ha terminado de comprar")
                    
  
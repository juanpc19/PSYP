#todos buscan numero (simular busqueda con cada hilo/persona tiene un bucle de busqueda)
#los que lo vayan encontrando se ponen en barrera a esperar hasta que todos lo encuentren 
#cuando todos esten en barrera salen        

import random
from threading import Barrier, Condition, Event, Thread
import time

class EscapeRoom(Thread):
    
    numeroAdivinar=random.randint(1,10000)
    evento=Event()
    
    def __init__(self, nombre, barrera=Barrier, cond=Condition):
        Thread.__init__(self, name=nombre)
         
        self.barrera=barrera
        self.cond=cond
        
    def run (self):
        while not self.evento.is_set():
            with self.cond:
                 
                numeroRandom=random.randint(1,10000)
                print("numero generado por:" , self.name, ": ", numeroRandom)
                
                if numeroRandom==self.numeroAdivinar:
                    print("El hilo", self.name, "ha adivinado la clave.")
                    EscapeRoom.evento.set()
                 
        print("El hilo", self.name, "esta esperando para salir.")
        time.sleep(3) 
        self.barrera.wait() 
        
        print("El hilo", self.name, "ha salido.")

        #FUNCIONA "BIEN" PERO LOS OTROS HILOS GENERAN NUMERO UNA VEZ MAS DE LA NECESARIA AUNQUE NO MODIFICAN NADA
 
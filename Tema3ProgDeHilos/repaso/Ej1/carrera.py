
import random
from threading import Barrier, Condition, Thread, Timer
import time



class Carrera(Thread):
    
    todosEnLinea=False
    salida=False
    
    def mensajeSalida():
        print("Salida!")
    
    def __init__(self, nombre, barrera=Barrier, cond=Condition, timer=Timer(3, mensajeSalida)):
        Thread.__init__(self, name=nombre)
        self.barrera = barrera
        self.cond=cond
        self.timer=timer
        
        
    def run(self):
        print("Hilo", self.name, "en posicion, esperando resto de hilos")
        self.barrera.wait()
        
        with self.cond:
            if Carrera.todosEnLinea==False:
                print("Todos en linea")
                Carrera.todosEnLinea=True
                self.cond.notify_all()
                
        with self.cond:
            if Carrera.salida==False:
                self.timer.start()
                
                Carrera.salida=True
                self.cond.notify_all()
                
        if Carrera.salida==True:
            inicio=time.time()
            print("El hilo", self.name, "ha salido")
            time.sleep(random.randint(1,2))
            final=time.time()
            print("El hilo", self.name, "ha llegado, ha tardado: ", final-inicio)
            
        
        
        
        
      
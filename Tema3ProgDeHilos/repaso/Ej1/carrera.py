import random
from threading import Barrier, Condition, Thread, Timer
import time



class Carrera(Thread):
    
    todosEnLinea=False
    salida=False
    
    def mensajeSalida():
        print("Salida!")
    
    def __init__(self, nombre, barrera=Barrier, cond=Condition):
        Thread.__init__(self, name=nombre)
        self.barrera = barrera
        self.cond=cond
       
        
        
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
                 
                print("3")
                time.sleep(random.randint(1,1))  
                print("2")
                time.sleep(random.randint(1,1))  
                print("1")
                time.sleep(random.randint(1,1))  
                print("salida!")
                Carrera.salida=True
                self.cond.notify_all()
                
        if Carrera.salida==True:
            inicio=time.time()
            print("El hilo", self.name, "ha salido")
            time.sleep(random.randint(1,2))
            final=time.time()
            print("El hilo", self.name, "ha llegado, ha tardado: ", final-inicio)
            
        
        
        
        
      
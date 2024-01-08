from threading import Thread
import time


#heredo poniendo nombre de clase a heredar entre parentesis, self=this.
class Raton(Thread):
    def __init__(self,nombre,tiempoAlimentacion):
        Thread.__init__(self, name=nombre)
        #self.nombre=nombre innecesario por poner name=nombre
        self.tiempoAlimentacion=tiempoAlimentacion
        
    def run (self):
        print("el raton", self.getName(), "empieza a comer")
        time.sleep(self.tiempoAlimentacion)#"delay"
        print("el raton", self.getName(), "ha termindao de comer")
        
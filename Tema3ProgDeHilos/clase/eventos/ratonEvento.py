#heredo poniendo nombre de clase a heredar entre parentesis, self=this.


import random
from threading import Event, Thread
import time


class Raton(Thread):
    def __init__(self,nombre,evento:Event):
        Thread.__init__(self, name=nombre) 
        self.evento=evento
        
    def run (self):
        while not self.evento.is_set():# si devuelve false sigue bucle
            self.evento.wait()#hace notifiy all
        self.evento.clear()#pone a false el evento
        print("el raton ", self.name, "esta comiendo")
        time.sleep(random.randint(1,3))
        print("el raton ", self.name, "termina de comer")
        self.evento.set()#pone a true el evento
        
        
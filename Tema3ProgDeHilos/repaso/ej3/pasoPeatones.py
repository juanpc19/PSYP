 
from threading import Barrier, Event, Thread, Timer


class PasoPeatones(Thread):
    
    
    def Cambio(evento):
        if evento.is_set():
            evento.clear()
            
            
            
        if not evento.is_set():
            evento.set()
        
            
    def __init__(self, nombre, barrera=Barrier, evento=Event, timer=Timer(5, Cambio)):
        self.name=nombre
        self.barrera=barrera
        self.evento=evento
        self.timer=timer
        
        
    def run(self):
        while True:
            
            if self.evento.is_set():
 
                self.barrera.abort()
                print("el hilo ", self.name, "esta cruzando")
             
            else:
                self.barrera.reset()
                self.barrera.wait()
                
                self.timer.start()
            
            
    
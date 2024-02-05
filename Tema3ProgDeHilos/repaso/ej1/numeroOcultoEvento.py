import random
from threading import Event, Lock, Thread


class NumeroOcultoEvento (Thread):
    
    numeroAdivinarGlobal=5
    numeroAdivinadoGlobal=False
    candado=Lock()

    def __init__(self,nombre, evento:Event):
        Thread.__init__(self, name=nombre)
        self.evento=evento
        
        
        
    def run(self):
        
        
        while True:
            NumeroOcultoEvento.candado.acquire()
            if not self.evento.is_set():
                numeroRandom=random.randint(0,12)
                
                print("soy el hilo: ",self.getName(), ". Numero producido:", numeroRandom)
                
                if numeroRandom==NumeroOcultoEvento.numeroAdivinarGlobal:
                    
                    NumeroOcultoEvento.numeroAdivinadoGlobal=True
                    print("soy el hilo: ",self.getName(), ". Numero encontrado")
                    self.evento.set()
            else:   
                print("numero no encontrado")
                NumeroOcultoEvento.candado.release()    
                
                
           
        
        
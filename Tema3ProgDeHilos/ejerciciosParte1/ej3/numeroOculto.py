#probe con lock y no funciona
import random
from threading import Thread

class NumeroOculto(Thread):
    
    numeroAdivinarGlobal=5
    numeroAdivinadoGlobal=False
    
    def __init__(self):
        Thread.__init__(self)
        
    def run (self):
        
        while (self.numeroAdivinadoGlobal==False):
            
            numeroRandom=random.randint(0,12)
            print(numeroRandom)
            
            if (numeroRandom==self.numeroAdivinarGlobal):
                self.numeroAdivinadoGlobal=True
                break #no parece hacer nada
            #deberia parar aqui la ejecucion de todos los hilos al cambiarse la global a true,
            #pero si ya hay un hilo ya iniciado en lo que se cambia el valor de la global 
            #en la iteracion actual, este puede seguir haciendo iteraciones, no se como leches parar eso,
            # SOS
            
                
                
        
#probe con lock y no funciona
import random
from threading import Thread

class NumeroOculto(Thread):
    
    numeroAdivinarGlobal=5
    numeroAdivinadoGlobal=False
    
    def __init__(self,nombre):
        Thread.__init__(self,name=nombre)
        
    def run (self):
        
        while NumeroOculto.numeroAdivinadoGlobal==False:
            
            numeroRandom=random.randint(0,12)
            print("soy el hilo: ",self.getName(), ". Numero producido:" , numeroRandom)
            
            if numeroRandom==NumeroOculto.numeroAdivinarGlobal:
                NumeroOculto.numeroAdivinadoGlobal=True
                break #hace break de hilo actual no de los demas
            
            #deberia parar aqui la ejecucion de todos los hilos al cambiarse la global a true,
            #pero si ya hay un hilo ya iniciado en lo que se cambia el valor de la global 
            #en la iteracion actual, este puede seguir haciendo iteraciones, no se como leches parar eso,
            # SOS
            
                
                
        
#probe con lock y no funciona
import random
from threading import Lock, Thread

class NumeroOculto(Thread):
    
    numeroAdivinarGlobal=5
    numeroAdivinadoGlobal=False
    candado=Lock()
    
    def __init__(self,nombre):
        Thread.__init__(self,name=nombre)
        
    def run (self):
        
        while NumeroOculto.numeroAdivinadoGlobal==False:
            
            #quizas probar con NumeroOculto.self.candado.acquire()
            numeroRandom=random.randint(0,12)
            print("soy el hilo: ",self.getName(), ". Numero producido:", numeroRandom)
            
            NumeroOculto.candado.acquire()
            if numeroRandom==NumeroOculto.numeroAdivinarGlobal:
                NumeroOculto.numeroAdivinadoGlobal=True
                break #hace break de hilo actual no de los demas
            NumeroOculto.candado.release()
            
            #deberia parar aqui la ejecucion de todos los hilos al cambiarse la global a true,
            #pero si ya hay un hilo ya iniciado en lo que se cambia el valor de la global 
            #en la iteracion actual, este puede seguir haciendo iteraciones, no se como leches parar eso,
            # SOS
            
                
                
        
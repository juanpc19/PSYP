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
            #hago lock antes de comprobacion y de producir numero y mostrarlo por pantalla 
            NumeroOculto.candado.acquire()
            numeroRandom=random.randint(0,12)
            
            print("soy el hilo: ",self.getName(), ". Numero producido:", numeroRandom)
            
            if numeroRandom==NumeroOculto.numeroAdivinarGlobal:
                
                NumeroOculto.numeroAdivinadoGlobal=True
                print("soy el hilo: ",self.getName(), ". Numero encontrado")
                
            #si tras comprobacion no coincide y necesito mas numeros hago release
            NumeroOculto.candado.release()
                
               
              
            
            
            
                
                
        
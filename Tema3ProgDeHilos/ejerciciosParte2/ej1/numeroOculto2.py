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
        
            
        # while True:
        #     NumeroOculto.candado.acquire()
        #     if not NumeroOculto.numeroAdivinadoGlobal:
        #         #NumeroOculto.candado.release()
        #         numeroRandom=random.randint(0,12)
        #         if numeroRandom==NumeroOculto.numeroAdivinarGlobal:
        #             #NumeroOculto.candado.acquire()
        #             NumeroOculto.numeroAdivinadoGlobal=True
        #             NumeroOculto.candado.release()
        #             print("el hilo", self.name, "ha acertado")
        #             break
        #         else:
        #             print ("el hilo", self.name, " ha generado el numero, ", numeroRandom, "y ha fallado")
                    
        #     else:
        #         NumeroOculto.candado.release()
        #         print ("otro hilo ya ha acertado")
        #         break
                
        
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
                
               
              
            
            
            
                
                
        
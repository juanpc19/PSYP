from threading import Thread

#cada hilo suma 1 al contador
class ContadorCompartido(Thread):
    
    contadorGlobal=1000
    
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        contador=0
        while(contador<self.contadorGlobal):
            contador+=1
            print(contador)
            
        
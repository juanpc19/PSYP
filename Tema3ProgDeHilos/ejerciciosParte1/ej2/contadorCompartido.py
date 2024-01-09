from threading import Thread

#cada hilo suma 1 al contador
class ContadorCompartido(Thread):
    
    contador=0
    
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        
        while ContadorCompartido.contador<1000:
            ContadorCompartido.contador+=1
            print(ContadorCompartido.contador)
            
    
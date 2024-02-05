import random
from threading import Event, Thread
import time


class Raton(Thread):
    def __init__(self,nombre,evento:Event):#recibe evento de main
        Thread.__init__(self, name=nombre) 
        self.evento=evento#hace k el evento de main sea el suyo propio, cada hilo hace esto por lo que siguen compartiendo evento
        
    def run (self):
        while not self.evento.is_set():# mientras el evento no este seteado (sea false) itero bucle (empieza en true porque asi lo indico en main)
            self.evento.wait()#pone en espera al hilo 
        self.evento.clear()#pone a false el evento al salir de bucle si evento es true
        
        
        print("el raton ", self.name, "esta comiendo")
        time.sleep(random.randint(1,3))
        print("el raton ", self.name, "termina de comer")
        self.evento.set()#pone a true el evento poruqe un raton ha acabado de comer
        
        
    #los hilos comparten evento recibido como param entrada, este evento esta a true por defecto el hilo que primero lo coja
    #pasara por la condicion del bucle y no entrara en este por lo que pasara directo a clear, de aqui pasara a simulacion 
    # de raton comiendo y tras esto hara set de evento momento en el que los otros hilos pelearan por el evento,
    #mientras un hilo hace esto los demas esperan por lo que los ratones comeran de 1 en 1
        
from threading import Barrier, Thread
import time
import random

class Caja(Thread):
    def __init__(self, nombre, barrera: Barrier):#recibo la barrera de main
        Thread.__init__(self, name=nombre)
        self.barrera = barrera # la asigno al atributo del constructor del hilo

    def run(self):
        self.barrera.wait()#todos los hilos tienen la misma barrera los 5 primeros hilos en empezar tomaran las 5 posiciones de la barrera
        #y hasta que no haya 5 hilos en la barrera no empezaran los procesos
        #una vez haya 5 hilos en barrera:
        print("Hilo", self.name, "entra en caja")#simularan entrar y salir de caja con delay de 3 segundos
        time.sleep(random.randint(1,3))
        print("Hilo", self.name, "sale de caja")
        #aqui acaba el hilo x liberando una posicion de barrera, una vez los 5 hilos acaben aqui 
        #habra liberadas 5 posiciones de la barrera lo que permitira a otros 5 hilos ejecutarse a la vez
        # una vez estos 
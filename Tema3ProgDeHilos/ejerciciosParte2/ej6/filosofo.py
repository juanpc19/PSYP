from threading import Condition, Thread
import time
import random

class Filosofo(Thread):
    cond = Condition()
    palillos = [False, False, False, False, False]

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            print("Filósofo", self.name, "está pensando")#simulacion de de pensar con delay
            time.sleep(random.randint(1,5))
            print("Filósofo", self.name, "deja de pensar")#cuando el filosofo deja de pensar
            with Filosofo.cond:#con el condition global
                while Filosofo.palillos[int(self.name)]:#si el palillo a la izq del filosofo esta libre
                    Filosofo.cond.wait()#lo ocupa, hace acquire y release antes y despue de esta linea por el with
                
                Filosofo.palillos[int(self.name)] = True#y pone el palillo a true para indicar que esta ocupado

                while Filosofo.palillos[(int(self.name)+1)%5]:#si el palillo a la der del filosofo esta libre
                    Filosofo.cond.wait()#lo ocupa, hace acquire y release antes y despue de esta linea por el with
                
                Filosofo.palillos[(int(self.name)+1)%5] = True#y pone el palillo a true para indicar que esta ocupado

            print("Filósofo", self.name, "está comiendo")#simulo el filosofo comiendo con delay
            time.sleep(random.randint(1,3))
            print("Filósofo", self.name, "termina de comer")

            with Filosofo.cond:#cuando el filosofo acaba de comer libero ambos palillos y lo notifico a todos los hilos 
                Filosofo.palillos[int(self.name)] = False
                Filosofo.palillos[(int(self.name)+1)%5] = False

                Filosofo.cond.notifyAll()
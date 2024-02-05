from threading import Barrier
from barrera import Caja
import time
import random

if __name__ == "__main__":
    barrera = Barrier(5)

    hilos = []
    for i in range(10):
        hilo = Caja(str(i), barrera)
        hilo.start()
        time.sleep(random.randint(1,5))#para ralentizar ejecucion hilos y ver funcionamiento mejor
        #aqui habra 5 hilos en ejecucion y 5 no
        hilos.append(hilo)

    for h in hilos:
        h.join()
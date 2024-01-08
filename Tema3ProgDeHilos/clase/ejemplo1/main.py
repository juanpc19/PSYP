from hilos1 import Hilos1


print("soy el hilo principal")

for i in range(0,10):
    hilo = Hilos1(i)
    hilo.start()
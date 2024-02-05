from filosofo import Filosofo

if __name__ == "__main__":

    hilos = []

    for i in range(5):
        hilo = Filosofo(str(i))
        hilo.start()
        hilos.append(hilo)

    for h in hilos:
        h.join()
from threading import Thread

#cada hilo suma 1 al contador
class ContadorCompartido(Thread):
    contadorGlobal=1000
    def __init__(self):
        
from threading import Thread


class Hilos1(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num=num
        
    def run (self):
        print("soy el hilo", self.num)
        
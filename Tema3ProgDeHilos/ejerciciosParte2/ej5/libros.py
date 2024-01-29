import random
from threading import Condition, Thread
import time


class Libro(Thread):
    
    libreria=[]
    con=Condition()    
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run(self):
        seleccionados=random.sample(range(9),2)#devuelve lista con 2 numeros random en rango estimado (9-1=8)sin repetir
        libro1=seleccionados[0]
        libro2=seleccionados[1]
        
        Libro.con.acquire()
        while Libro.libreria[libro1] or Libro.libreria[libro2]:
            print("el estudiante", self.name, "esta esperando los libros", libro1, libro2)
            Libro.con.wait()
        
        Libro.libreria[libro1]=True
        Libro.libreria[libro2]=True
        Libro.con.release()
        
        print("el estudiante", self.name, "esta leyendo los libros", libro1, libro2)
        time.sleep(random.randint(3,5))
        print("el estudiante", self.name, "esta leyendo los libros", libro1, libro2)
        
        Libro.con.acquire()
        Libro.libreria[libro1]=False
        Libro.libreria[libro2]=False
        Libro.con.notifyAll()
        Libro.con.release()
        print("el estudiante", self.name, "ha devuelto los libros", libro1, libro2)


    

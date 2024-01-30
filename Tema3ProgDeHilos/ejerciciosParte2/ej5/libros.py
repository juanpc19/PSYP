import random
from threading import Condition, Thread
import time


class Libro(Thread):
    
    libreria=[]
    con=Condition()    
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run(self):
        while True:
            seleccionados=random.sample(range(9),2)#devuelve lista con 2 numeros random en rango estimado (9-1=0,8)sin repetir
            libro1=seleccionados[0]#libro1=random 1
            libro2=seleccionados[1]#libro2=random 2
            
            #bloqueo hilo antes de seccion critica
            Libro.con.acquire()
            while Libro.libreria[libro1] or Libro.libreria[libro2]:#si uno de los 2 es true
                print("el estudiante", self.name, "esta esperando los libros", libro1, libro2)
                Libro.con.wait()#bloquea hilo hasta notify
            
            Libro.libreria[libro1]=True#el estudiante/hilo "ocupa" los 2 libros
            Libro.libreria[libro2]=True
            Libro.con.release()#una vez cambiados libros a "ocupados" libero el hilo que los ocupa
            
            #se muestra con mensaje la lectura de los libros al empezar
            print("el estudiante", self.name, "esta leyendo los libros", libro1, libro2)
            time.sleep(random.randint(3,5))
            print("el estudiante", self.name, "termina de leer los libros", libro1, libro2)
            #y al terminar
            
            #bloqueo hilo antes de cambiar variable que afecta a condicion de seccion critica
            Libro.con.acquire()
            Libro.libreria[libro1]=False#"libero" los 2 libros
            Libro.libreria[libro2]=False
            Libro.con.notifyAll()#notifico la liberacion a todos los hilos
            Libro.con.release()#libero el lock
            #notifico por pantalla
            print("el estudiante", self.name, "ha devuelto los libros", libro1, libro2)
            
            #los estudiantes requieren 2 libros especificos no 2 cualquiera solo cuando estos estan libres a la vez, los coge,
            #tras leerlos, un hilo suelta los 2 libros y si otro hilo requiere esos 2 los coge pero si 1 de los 2 requeridos no
            #esta disponible no coge ninguno y otro hilo puede cogerlos
             
             

    

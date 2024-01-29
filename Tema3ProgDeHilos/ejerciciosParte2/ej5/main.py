from libros import Libro

if __name__=="__main__":
   
    hilos=[]
    
    for i in range(9):
        Libro.libreria.append(False)
        
    for i in range(4):
        hilo = Libro(str(i))
        hilo.start()
        hilos.append(hilo)
    
    for h in hilos:
        h.join()

 
    
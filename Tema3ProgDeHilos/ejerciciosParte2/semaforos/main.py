from ejemplo1 import Cajero

if __name__=="__main__":
    lista=[]
    for i in range (20):
        hilo=Cajero(str(i))
        hilo.start()
        lista.append(hilo)
        
    for h in lista:
        h.join()
        
    print ("fin de main")
        
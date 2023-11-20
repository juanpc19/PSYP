from multiprocessing import *
import time

def sumatorio(numero):
    if numero>=1:
        sumados=0
        for i in range(1,numero+1):
            sumados+=i
        return (sumados)
    else:
        print ("Error introduzca numero igual o mayor a 1.")
        

#primera mitad igual que el 1 segunda mitad de prueba pool
if __name__ == "__main__":
  
    
    pool=Pool(processes=3)
    pool2=Pool(processes=10)
    numeros= [1,2,3,4,5,6,7,8,9,10]
    
    
    inicio=time.time()
    resultados=pool.map(sumatorio,numeros)
    fin=time.time()
    
    print(resultados)
    print(fin-inicio)
    
    inicio=time.time()
    resultados=pool2.map(sumatorio,numeros)
    fin=time.time()

    print(resultados)
    print(fin-inicio)
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
        
#funcione lee archivo manda numeros a funcion 

#primera mitad igual que el 1 segunda mitad de prueba pool
if __name__ == "__main__":
  
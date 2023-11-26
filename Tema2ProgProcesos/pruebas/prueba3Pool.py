from multiprocessing import Pool
import time

#si 2 parametros entra usar dicc con tublas
def doble(num):
    return 2*num

if __name__ == "__main__":
    inicio=time.time()
    
    pool=Pool(processes=3)
    numeros= [1,2,3,4,5,6,7,8,9,10]
    
    resultados=pool.map(doble,numeros)
    
    fin=time.time()

    pool.close()
    print(resultados)
    print(fin-inicio)
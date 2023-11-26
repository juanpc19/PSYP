from multiprocessing import Pool, Process
import time
#funcion que devuelve sumatorio de 2 numeros dados como param entrada
def sumatorio(numero1,numero2):
    # si numero 2 menor que numero 1 intercambio valores para que for funcione
    if numero2<numero1:
        numero1,numero2=numero2,numero1
    #si ambos numeros son igual o mayor a 1
    if numero1>=1 and numero2>=1:
        sumados=0
        #recorro el rango sumando de numero1 a numero 2 incluido
        for i in range(numero1,numero2+1):
            sumados+=i
        #y hago print de sumados por terminal
        return sumados
    else:
        print ("Error introduzca numero igual o mayor a 1.")
       
if __name__=="__main__":
    
    piscinazo=Pool(processes=15)
    piscinazo2=Pool(processes=50)
    argumentos = [(5, 1), (1, 1), (1, 6)]
    
    inicio=time.time()
    resultado=piscinazo.starmap(sumatorio, argumentos)
    final=time.time()
    
    print(resultado)
    print(final-inicio)
    
    
    inicio2=time.time()
    resultado=piscinazo2.starmap(sumatorio, argumentos)
    final2=time.time()
    
    print(resultado)
    print(final2-inicio2)
from multiprocessing import Pool
from time import *

def cuentaVocales(vocal):
    
    fichero="Tema2ProgProcesos\\ejercicios\\ficheros\\vocales.txt"
    contador=0
    
    try:
        with open(fichero, 'r') as f:
                #vuelco archivo en string texto
                texto=f.read()
                #cuento ocurrencias de vocal en texto y las asigno a contador
                contador=texto.count(vocal)
                #devuelvo contador
        return contador
                   
    except FileNotFoundError:   
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)
        

if __name__ == "__main__":
    #creo pool de 5 procesos para 5 vocales
    pool=Pool(processes=5)
    #proveo lista vocales
    vocales=["a","e","i","o","u"]
  
    inicio=time()
    #lanzo pool y recojo resultados    
    resultados=pool.map(cuentaVocales, vocales)
    final=time()
    
    #print resultados
    print(resultados, (final-inicio))   
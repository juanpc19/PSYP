from multiprocessing import Pool, Process
#.read(1) lee un char
def cuentaVocales(fichero, vocales):
    
    dict={}
    contador=0
    
    try:
        with open(fichero, 'r') as f:
            #vocal de la que hare check
            for vocal in vocales:
                #siguiente linea fichero
                for linea in f:
                    contador=linea.count(vocal)
                    dict[vocal]=contador
                    #siguiente letra en linea actual
                    # for letra in linea:
                    #     if letra==vocal:    
                    #         contador=linea.count(vocal)
                    #         return contador
                
    except FileNotFoundError:   
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)
        
    return dict

if __name__ == "__main__":
    
    fichero="Tema2ProgProcesos\\ejercicios\\ficheros\\vocales.txt"

    pool=Pool(processes=5)
    vocales=["a","e","i","o","u"]
    
    resultados=pool.map(cuentaVocales, (fichero, vocales))
 
    print(resultados)
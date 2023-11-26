 #productor
def leerFichero(fichero):
    listaNumeros=[]
    try:
        #apertura archivo con autocierre requiere indentacion sig linea
        with open(fichero, 'rt') as f:
            #recorro archivo leyendo todas las lineas
            for linea in f.readlines():
                #las voy añadiendo a lista quitandoles el salto de lina con strip
                listaNumeros.append(linea.strip())
    except FileNotFoundError:   
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)
        
    return listaNumeros

#consumidor
def sumatorio(numero):
    if numero>=1:
        sumados=0
        for i in range(1,numero+1):
            sumados+=i
        return (sumados)
    else:
        print ("Error introduzca numero igual o mayor a 1.")
        
#productor
def leerFicheroCola(cola):
   
    try:
        #apertura archivo con autocierre requiere indentacion sig linea
        with open("ficheros/numeros.txt", 'rt') as f:
            #recorro archivo leyendo todas las lineas
            for linea in f.readlines():
                #las voy añadiendo a cola quitandoles el salto de lina con strip
                cola.put(linea.strip())
            #si no hay mas elementos que añadir a la cola añado None para indicar a proceso final de cola
            cola.put(None)
                
    except FileNotFoundError:   
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

#consumidor
def sumatorioCola(cola):
    #cojo primer item de la cola
    itemCola=cola.get()
    #bucle se ejecuta mientras haya items en cola diferente a none
    while itemCola is not None:
        sumados=0
        #hago sumatorio del itemCola actual con bucle for
        for i in range(1,itemCola+1):
            sumados+=i
        #muestro reultado sumatorio en print (no se hacer return de varios sumatorios, lista resultados?))
        print(sumados)
        #cojo siguiente item en cola y repito todo hasta que no queden items en cola o este ultimo se none
        itemCola=cola.get()
        
        #funcion que devuelve sumatorio de 2 numeros dados como param entrada
        
def sumatorioRango(numero1,numero2):
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
        print (sumados)
    else:
        print ("Error introduzca numero igual o mayor a 1.")
       
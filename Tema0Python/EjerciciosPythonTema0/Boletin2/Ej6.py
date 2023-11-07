#declaro un diccionario vacio
diccionario={}
#recogo valor para la frase
frase=input("Introduzca una frase con la que construir el diccionario: ")
#la divido en una lista de strings con frase.split(" ") y la guardo en listaPalabras
listaPalabras=frase.split(" ")
#print(listaPalabras)

#recorro la lista de palabras en toda su longitud haciendo uso de len(lista)
for palabra in range (0,len(listaPalabras)):
    #si la palabra en posicion actual de la lista no esta en el diccionario
    if (listaPalabras[palabra]) not in diccionario:
        #la agrego y le doy a su valor valor igual a 1
        diccionario[listaPalabras[palabra]]=1
        #si por el contrario ya esta en la lista sumo +1 a su valor
    else:
        diccionario[listaPalabras[palabra]]+=1     
        
#recorro diccionario extrayendo clave y valor de cada posicion haciendo uso de .items()
for clave, valor in diccionario.items():
    print("La palabra:", clave,", aparece", valor, "veces en el diccionario.")


    
    
    
    

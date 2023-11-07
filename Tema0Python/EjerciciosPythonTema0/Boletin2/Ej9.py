#creo diccionario con valores
puntuacionesScrabble = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
}
#declaro variables y las inicializo
palabra=""
puntuacionPalabra=0

#doy valor a palabra con input teclado
palabra=input("Introduzca una palabra:")

#recorro diccionario a traves de claves
for clave in puntuacionesScrabble:    
    #si clave actual esta en cadena
    if clave in palabra:
        #añado su valor correspondiente a puntuacionPalabra
        puntuacionPalabra+=puntuacionesScrabble[clave]
        
#hago print de la puntuacion
print(puntuacionPalabra)
#importo modulo random para usar random.randint (numero int random)
import random

#me creo una lista vacia
lista=[]

#bucle que itera 10 veces 
for contador in range(0,10):
    #creo variable numero y le doy valor random de 1 a 100
    numero=random.randint(1,100)
    #pongo valor de numero en ultima posicion de la lista con append
    lista.append(numero)

#al salir del bucle hago print de la lista
print (lista)

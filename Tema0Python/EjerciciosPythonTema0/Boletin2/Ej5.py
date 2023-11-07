import random

lista=[]

#creo lista de 100 numeros
for contador in range(0,100):
    #creo variable numero y le doy valor random de 1 a 10
    numeroRandom=random.randint(1,10)
    #pongo valor de numero en ultima posicion de la lista con append
    lista.append(numeroRandom)

numero=int (input("Introduzca un numero entero a buscar en la lista: "))

#cuento las veces que aparece el numero en la lista con lista.count(valor a buscar)
print("El numero introducido aparece en la lista", lista.count(numero), "veces.")

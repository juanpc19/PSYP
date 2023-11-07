lista=[]

#solicito 10 numero para rellenarla con append
for contador in range(0,8):
    numero=int (input("Introduzca un numero entero: "))
    lista.append(numero)

#solo añado sort para ordenar, si ente parantesis lleva reverse=True hace mayor a menor
lista.sort(reverse=True)

print(lista) 

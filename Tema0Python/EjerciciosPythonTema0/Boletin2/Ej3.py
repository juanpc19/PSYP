lista=[]

#solicito 10 numero para rellenarla con append
for contador in range(0,8):
    numero=int (input("Introduzca un numero entero: "))
    lista.append(numero)
   
print(lista) 

for contador in range(0,8):
    if lista[contador]%2==0:
        print("Par:", lista[contador])
    else:
        print("impar:", lista[contador])
        
        
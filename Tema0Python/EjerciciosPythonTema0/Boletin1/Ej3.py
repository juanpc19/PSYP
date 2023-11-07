#declaro variables y las inicializo a 0
numeroIntroducido=0
sumaTotal=0

#bucle while se ejecuta mientras numero introducido no sea negativo
while numeroIntroducido>=0:
    numeroIntroducido=int(input("Introduzca un numero entero positivo a sumar, o un numero entero negativo para parar el programa:"))
    #si el numero introducido es positivo se lo sumo al total, de lo contrario solo lo uso para decidir salida de bucle sin sumarlo al total
    if numeroIntroducido>=0:
        sumaTotal+=numeroIntroducido
#muestro la suma total   
print(sumaTotal)

print("cerrando...")
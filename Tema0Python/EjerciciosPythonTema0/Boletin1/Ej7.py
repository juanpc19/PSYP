#declaro variables y las inicializo a 0
numeroIntroducido=int (input("Introduzca el numero que desea saber si es primo o no:"))
esPrimo=True

if numeroIntroducido<2:
        esPrimo=False
        
for contador in range (2,numeroIntroducido):
    if numeroIntroducido%contador==0:
        esPrimo=False
        break

#ternario
#respuesta=("El numero introducido es primo.") if esPrimo==True else ("El numero introducido no es primo.")  
print("El numero introducido es primo.") if esPrimo==True else ("El numero introducido no es primo.")  

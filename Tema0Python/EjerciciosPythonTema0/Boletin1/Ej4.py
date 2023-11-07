#importo modulo random
import random
#doy a numero aleatorio valor igual a un numero aleatorio entre 0 y 100 con uso de modulo/funcion random.radint()
numeroRandom=random.randint(0,100)
#print para testeo
print(numeroRandom)

#declaro variables y las inicializo a 0
numeroIntroducido=0
sumaTotal=0

#bucle while se ejecuta mientras numero introducido no sea -1 y diferente del numero secreto aleatorio
while numeroIntroducido!=-1 and numeroIntroducido!=numeroRandom:
    
    #doy a numero introducido valor introducido por teclado aplicandole cast
    numeroIntroducido=int(input("Introduzca un numero entero para intentar adivinar el numero secreto aleatorio o -1 para rendirse:"))
    
    #si es negativo comunico a jugador su rendicion
    if numeroIntroducido==-1:
        print("Usted se ha rendido.")
    #de lo contrario comunico a jugador si su numero es menor o mayor al numero secreto
    else:
        if numeroIntroducido>numeroRandom:
            print("El numero secreto es menor que el numero introducido.")
        elif numeroIntroducido<numeroRandom:
            print("El numero secreto es mayor que el numero introducido.")
        #si no es ni mayor ni menor comunico victoria al jugador antes de cerrar bucle
        else:
            print("¡Felicidades, acertaste el numero secreto!")

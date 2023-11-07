#declaro variables y las inicializo a 0
numeroN=0
siguienteNumero=1

#doy valor a numeroN con valor de usuario introducido por teclado
numeroN=int(input("Introduzca un numero entero hasta el que quiera contar desde el 1:"))

#bucle while se ejecuta mientras siguienteNumero no sea mayor a numeroN
while siguienteNumero<=numeroN:
    print(siguienteNumero)
    siguienteNumero+=1
    
    
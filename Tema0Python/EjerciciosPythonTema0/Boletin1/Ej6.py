#declaro variables y las inicializo a 0
numeroIntroducido=int (input("Introduzca el numero cuyo factorial desea:"))
factorial=1
contador=1
while contador<numeroIntroducido:
    #print("cuenta",contador)
    #print("facto",factorial)
    factorial+=factorial*contador
    contador+=1

print("El factorial de",numeroIntroducido,"es:",factorial)

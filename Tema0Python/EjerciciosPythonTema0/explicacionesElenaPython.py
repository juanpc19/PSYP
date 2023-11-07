print ("Hola mundo")

a=1
b=2
suma = a+b
print (suma)

a1= float (input("Introduzca un numero"))
#cast para a 2 porque por defecto string 
a2= float (input("Introduzca un numero"))

suma = a1+a2
print (suma)

#condicion sin parentesis bloque instrucciones tabulado tras 2 puntos
if a % 2==0:
    print("numero es par")
else:   
    print("el numero es impar")
    
#el no es como java !=
if a % 2 !=0:
       print("numero es par") 
    
#and or se esbriben tal cual sin simbolos 
if a>0 and a <=100:
        print ("numero entre 1 y 100")
else:   
    print("el numero es impar")
#el else if es asi:    
if a>=0 and a<5:
    print("suspenso")
elif a>=5 and a<6:
    print("suficiente")
    
a=1

p="par" if a%2==0 else "impar"
#coma para separar partes de un print
print("su numero es:", p)
    
#ejemplo bucle while 
num=5
i=0
while a<=num:
    print(i)
    suma+=i
    i=+1
print(suma)

#contador por defecto de 1 en 1 
for contador in range(1,101):
    print(contador)
    
#contador de 3 en 3
for contador in range(1,101,3):
    print(contador)

#contador por defecto de 1 en 1 hacia atras
for contador in range(100,1,-1):
    print(contador)

#
cadena="hola"
for caracter in cadena:
    print(caracter)

#funcion
def suma(num1, num2):
    res=num1+num2
    return res
       
num3=3        
def par(num):
    if num % 2==0:
        print("numero es par")
    else:
        print("el numero es impar")
    
    
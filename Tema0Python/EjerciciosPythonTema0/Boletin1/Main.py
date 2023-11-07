from Ej9 import *
from Ej10 import *
from Ej11 import *
from Ej12 import *

#Ej9
num1 = int (input("Introduzca un numero:"))
num2 = int (input("Introduzca otro numero:"))

#para ordenar de menor a mayor intercambiando valores
if num1>num2:
    num1,num2=num2,num1
    
print("Este es el rango de esos numeros ordenados menor a mayor:")
#no hay que indicar tipo parametro entrada en python
rango(num1,num2)

######################################################################################################
#Ej10
num1 = int (input("Introduzca un numero:"))
num2 = int (input("Introduzca otro numero:"))

print("Este es el maximo de esos 2 numeros:")
#no hay que indicar tipo parametro entrada en python
print(maximo(num1,num2))

######################################################################################################
#Ej11
cadena=input("Introduzca una palabra:")

for letra in (cadena):  
    print("La letra", letra, "Es vocal.") if esVocal(letra) else print("La letra", letra, "No es vocal.")

######################################################################################################
#Ej12
num1 = int (input("Introduzca un numero:"))
num2 = int (input("Introduzca otro numero:"))
operacion = int (input("""Introduzca la operacion que desea realizar:
                  1.Suma.
                  2.Resta.
                  3.Multiplicacion.
                  4.Division."""))

print(calculadora(num1,num2,operacion))


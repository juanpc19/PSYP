from CuentaCorriente import *

dni=""
nombre=""
saldo=0.0

dni=input("Introduzca un DNI:")
nombre=input("Introduzca un nombre:")
saldo=float(input("Introduzca saldo inicial de cuenta:"))                       
cuenta1 = CuentaCorriente(dni,nombre,saldo)

dni=input("Introduzca un DNI:")
nombre=input("Introduzca un nombre:")
saldo=float(input("Introduzca saldo inicial de cuenta:"))      
cuenta2 = CuentaCorriente(dni,nombre,saldo)

dni=input("Introduzca un DNI:")
saldo=float(input("Introduzca saldo a ingresar en la cuenta:"))      
cuenta1.ingresarDinero(dni,saldo)

dni=input("Introduzca un DNI:")
saldo=float(input("Introduzca saldo a ingresar en la cuenta"))      
cuenta2.ingresarDinero(dni,saldo)

dni=input("Introduzca un DNI:")
saldo=float(input("Introduzca saldo a sacar de la cuenta:"))      
cuenta1.sacarDinero(dni,saldo)

dni=input("Introduzca un DNI:")
saldo=float(input("Introduzca saldo a sacar de la cuenta:"))      
cuenta2.sacarDinero(dni,saldo)

print(cuenta1.__str__())
print(cuenta2.__str__())

obj1IgualObj2=cuenta1.__eq__(cuenta2)
print(obj1IgualObj2)

obj1MenorObj2=cuenta2.__lt__(cuenta1)
print(obj1MenorObj2)

obj1MenorObj2=cuenta1.__lt__(cuenta2)
print(obj1MenorObj2)









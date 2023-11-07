# Nos piden hacer un programa que gestione una serie de productos. Los productos tienen los siguientes atributos:
# Nombre
# Precio
# Tenemos dos tipos de productos:
# Perecedero: tiene un atributo llamado días a caducar.
# No perecedero: tiene un atributo llamado tipo.
# Tendremos una función llamada calcular, y que según la clase hará una cosa u otra. A esta función le pasaremos un número que será la cantidad de productos:
# En Producto, simplemente sería multiplicar el precio por la cantidad de productos pasados y devolverá el resultado.
from Producto import*
from Perecedero import * 
from NoPerecedero import*

cantidad=5

prod=Producto("lapiz",1.0)
print(prod.__str__())
print(prod.calcular(cantidad))
print()

pere=Perecedero("queso",2.0,2)
print(pere.__str__())
print(pere.calcular(cantidad))
print()

noPere=NoPerecedero("zapatillas nike",3.0,"Zapato")
print(noPere.__str__())
print(noPere.calcular(cantidad))
print()


print("Primer producto menor que segundo producto.") if prod.__lt__(pere) else print ("Primer producto no es menor que segundo producto.")

print("Primer producto menor que segundo producto.") if noPere.__lt__(pere) else print ("Primer producto no es menor que segundo producto.")
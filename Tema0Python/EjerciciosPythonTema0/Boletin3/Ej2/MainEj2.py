from Libro import * 

libro1=Libro("siu", "pepe", 1, 0)

libro2=Libro("siu", "pepe", 1, 0)

libro3=Libro("nou", "pepe", 1, 0)

libro4=Libro("nou", "pepa", 1, 0)

print(libro1.__str__())
print("prestado") if libro1.prestamo() else print ("no prestado")
    
print(libro1.__str__())
print("prestado") if libro1.prestamo() else print ("no prestado")


print(libro1.__str__())
print("Si devuelto") if libro1.devolucion() else print ("no devuelto")

print(libro1.__str__())
print("Si devuelto") if libro1.devolucion() else print ("no devuelto")

print(libro1.__str__())

print("iguales") if libro1.__eq__(libro2) else print ("no iguales")
print(libro1.__str__())
print(libro2.__str__())

print("iguales") if libro1.__eq__(libro4) else print ("no iguales")
print(libro1.__str__())
print(libro4.__str__())

lMenorL=libro1.__lt__(libro2)
print(lMenorL)

lMenorL=libro1.__lt__(libro4)
print(lMenorL)

lMenorL=libro4.__lt__(libro1)
print(lMenorL)



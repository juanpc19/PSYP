
f=open("EjerciciosPythonTema0\Boletin5\Ej2\cosaEj2.txt", "w")

inputUsuario=input("Introduzca su texto:")

while inputUsuario!= "fin":
    
    f.write(inputUsuario)
    print(inputUsuario)
    inputUsuario=input("Introduzca su texto:")
    
f.close
print("cambio y corto")
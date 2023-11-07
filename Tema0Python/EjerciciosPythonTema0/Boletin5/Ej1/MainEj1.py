edadMedia=0
estaturaMedia=0
contador=0
 
#abro fichero en modo escritura 
f=open('EjerciciosPythonTema0\Boletin5\Ej1\Alumnos.txt', 'w')

f.write("juan 22 1.77\n")

f.write("luis 21 1.80\n")

f.write("pedro 20 1.73\n")

f.close()
#hasta aqui funciona
f=open('EjerciciosPythonTema0\Boletin5\Ej1\Alumnos.txt', 'rt')

for linea in f.readlines():
    nombre,edad,altura=(linea.split())
    #print(nombre, edad, altura)
    print(nombre)
    contador+=1
    edadMedia+=int(edad)
    estaturaMedia+=float(altura)
    
f.close()

edadMedia/=contador
print ("La edad media es de:", str(edadMedia))

estaturaMedia/=contador
print("La estatura media  es de:", str(estaturaMedia))
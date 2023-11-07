#importo las funciones de su clase
from FuncionesEj7 import *

#declaro e inicializo el diccionario y las variables
agenda={}
contacto=""
telefono=0
opcion=4

#instancio la clase en el objeto para usar sus metodos
funciones_obj = FuncionesEj7()

#mientras la opcion sea diferente a 0
while opcion !=0:
      
      #hago print de menu y recojo nuevo valor para opcion
      funciones_obj.menu()
      opcion=int(input())
      
      #si la opcion es 1 solicito datos y agrego contacto dando datos a funcion al llamarla con el objeto e igualando agenda al return que me hara la funcion 
      if opcion==1:
            contacto=input("Introduzca el contacto que desea agregar:")
            telefono=input("Introduzca el numero de telefono que desea agregar:")
            agenda=funciones_obj.agregarContacto(contacto,telefono,agenda)
           
      #si la opcion es 2 solicito datos y borro contacto dando datos a funcion al llamarla con el objeto e igualando agenda al return que me hara la funcion     
      if opcion==2:
            contacto=input("Introduzca el contacto que desea borrar:")
            agenda=funciones_obj.borrarContacto(contacto,agenda)
            
      #si la opcion es 3 solicito datos y busco contacto dando datos a funcion al llamarla y esta me mostrara el contacto y su telefono
      if opcion==3:
            contacto=input("Introduzca el contacto que desea buscar:")
            funciones_obj.buscarContacto(contacto,agenda)
            








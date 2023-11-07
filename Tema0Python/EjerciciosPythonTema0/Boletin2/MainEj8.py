#importo las funciones
from FuncionesEj8 import *

#declaro e inicializo el diccionario y las variables
listaVentas={}
producto=""
cantidadVendida=0
totalVentas=0 
opcion=4

#instancio la clase en el objeto para usar sus metodos
funciones_obj = FuncionesEj8()

#mientras la opcion sea diferente a 0
while opcion !=0:
      
      #hago print de menu y recojo nuevo valor para opcion
      funciones_obj.menu()
      opcion=int(input())
      
      #si la opcion es 1 solicito datos y agrego producto dando datos a funcion al llamarla con el objeto e igualando listaVentas al return que me hara la funcion 
      if opcion==1:
          producto=str(input("Introduzca el producto vendido:"))
          cantidadVendida=int(input("Introduzca la cantidad vendida:"))
          listaVentas=funciones_obj.agregarVenta(producto, cantidadVendida, listaVentas)
          print(listaVentas)
        
      #si la opcion es 2 solicito datos y llamo a funcion con el objeto e igualo totalVentas al return que me hara la funcion   
      elif opcion==2:
          producto=input("Introduzca el producto cuyas ventas totales quiere saber:")
          totalVentas=funciones_obj.cuentaVentas(producto, listaVentas)
          print(totalVentas)
      
      
           
            
      
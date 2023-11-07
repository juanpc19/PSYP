class FuncionesEj7:
    
    #print de menu
    def menu(self):
        
        print("""
              Libreta de direcciones:
               1. Agregar contacto.
               2. Eliminar contacto.
               3. Buscar contacto."""
               )
    
    #1.agregar contacto si no esta ya presente en la lista y devuelve esta modificada en return
    def agregarContacto(self,contacto,telefono,agenda):
         
        if contacto not in agenda:
            agenda[contacto]=telefono  
            print("El contacto ha sido añadido a la lista.")
        else:
            print("El contacto ya esta en la lista.")
            
        return agenda
            
    #2.borrar contacto si esta presente en la lista lo borro usando del y y devuelvo lista modificada en return
    def borrarContacto(self,contacto,agenda):      
       
        if contacto in agenda:
            del agenda[contacto]  
            print("El contacto ha sido borrado de la lista.")  
        else:
            print("El contacto no esta en la lista.")
        return agenda
    
    #3.si el contacto buscado esta en la agenda lo muestro junto a su telefono con print
    def buscarContacto(self,contacto,agenda):     
        if contacto in agenda:
            print("El numero de",contacto,"es:", agenda[contacto])
        else:
            print("El contacto no esta en la lista.")  

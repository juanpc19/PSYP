from Empleado import*
class Directivo(Empleado):
  
    def __init__(self):
        super().__init__()
  
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def setNombre(self, nombre):
        self.nombre=nombre
        
    def getNombre(self):
        resultado=self.nombre
        
        return resultado
    
    def __str__(self):
        cadena=super().__str__() + " -> Directivo"
    
        return cadena
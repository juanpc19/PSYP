class Empleado:
  
    def __init__(self):
        self.nombre=""
  
    def __init__(self, nombre):
        self.nombre=nombre
        
    def setNombre(self, nombre):
        self.nombre=nombre
        
    def getNombre(self):
        resultado=self.nombre
        
        return resultado
    
    def __str__(self):
        cadena= "Empleado" + " " + self.nombre
  
        return cadena
    
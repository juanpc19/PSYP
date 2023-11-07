class Animal:
    
    def __init__(self, nombre, numeroPatas):
        self.nombre=nombre
        self.numeroPatas=numeroPatas
        
    def habla(self):
        cadena=""
        
        return cadena
    
    def __str__(self):
        
        cadena="Me llamo " + self.nombre + ", tengo " + str(self.numeroPatas) + " patas y sueno asi: " + self.habla()
        
        return cadena
    
    
        
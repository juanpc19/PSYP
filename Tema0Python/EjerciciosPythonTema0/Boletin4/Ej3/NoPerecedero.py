from Producto import*
class NoPerecedero(Producto):
    
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo=tipo
        
    def calcular(self, cantidad):
        resultado=super().calcular(cantidad)
        
        return resultado
    
    def __str__(self):
        cadena=super().__str__() + "\nTipo: " + self.tipo
        
        return cadena
    
    def __lt__(self, objeto):
        menor=super().__lt__(objeto)
        
        return menor
class Producto:
    
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio
        
    def calcular(self, cantidad):
        resultado=self.precio*cantidad
        
        return resultado
    
    def __str__(self):
        cadena="Nombre: " + self.nombre + "\nPrecio: " + str(self.precio)
        
        return cadena
    
    def __lt__(self, objeto):
        menor=False
        if self.nombre<objeto.nombre:
            menor=True
        
        return menor
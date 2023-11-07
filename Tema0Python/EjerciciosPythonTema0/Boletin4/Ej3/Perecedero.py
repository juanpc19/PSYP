from Producto import*
class Perecedero(Producto):
    
    def __init__(self, nombre, precio, diasCaducar):
        super().__init__(nombre, precio)
        self.diasCaducar=diasCaducar
        
    def calcular(self, cantidad):
        resultado=super().calcular(cantidad)
        
        if self.diasCaducar==1:
            resultado/=4
        elif self.diasCaducar==2:
            resultado/=3
        elif self.diasCaducar==3:
            resultado/=2
            
        return resultado
    
    def __str__(self):
        cadena=super().__str__() + "\nDias para caducar: " + str(self.diasCaducar)
        
        return cadena
    
    def __lt__(self, objeto):
        menor=super().__lt__(objeto)
        
        return menor
        
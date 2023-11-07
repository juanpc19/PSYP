class Articulo:
    
    def __init__(self, nombre, precio, cuantosQuedan):
        self.nombre=nombre
        self.precio=precio
        self.iva=21
        self.cuantosQuedan=cuantosQuedan
        
    def getPVP(self):
        pvp=self.precio+(self.precio*(self.iva/100))
        
        return pvp
    
    def getPvpDescuento(self,pvp,descuento):
        pvpDescuento=pvp-(pvp*(descuento/100))
       
        return pvpDescuento
        
    def almacenar(self, cantidad):
        self.cuantosQuedan+=cantidad
    
    def vender(self, cantidad):
        posible=False
        if cantidad<=self.cuantosQuedan:
            self.cuantosQuedan-=cantidad
            posible=True
            
        return posible
    
    def __str__(self):
        cadena = "Nombre: " + self.nombre + "\nPrecio: " + str(self.precio) + "\nIVA: " + str(self.iva) + "\nCuantos quedan: " + str(self.cuantosQuedan)
        
        return cadena  
        
    def __eq__(self, articulo):
        iguales=False
        if self.nombre==articulo.nombre:
            iguales=True
            
        return iguales
    
    def __lt__(self, articulo):
        menor=False
        if self.nombre<articulo.nombre:
            menor=True
            
        return menor
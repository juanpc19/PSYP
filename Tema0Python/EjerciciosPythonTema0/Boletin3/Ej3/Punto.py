class Punto:
    
    def __init__(self, x,y):
        self.x=x
        self.y=y
        
    def __str__(self):
        cadena= "Coordenada X: " + str(self.x) 
        cadena+=", Coordenada Y: "+ str(self.y)
        
        return cadena
    
    def setXY(self,x,y):
        self.x=x
        self.y=y
        
    def desplaza(self,dx,dy):
        self.x+=dx
        self.y+=dy
    
    def distancia(self, otroPunto):
        resultado=self.x-otroPunto.x
        
        return resultado    
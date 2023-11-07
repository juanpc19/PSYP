from Animal import *

class Perro(Animal):
    
    def __init__(self, nombre, numeroPatas):
        super().__init__(nombre, numeroPatas)
        
    def habla(self):
        cadena="Guau."
        
        return cadena
    
    def __str__(self):
        #extraigo nombre clase con siguiente linea y lo añado a la cadena
        nombreClase= self.__class__.__name__
        # cojo la siguiente cadena con + super().__str__() 
        #cadena="Me llamo " + self.nombre + ", tengo " + str(self.numeroPatas) + " patas y sueno asi: " + self.habla()
        # y la parte de + self.habla() se llama sola al llamar al super 
        # porque este llama a self.habla() dentro de la llamada super().__str__() 
        # pero aqui no herada del super al no especificar super por lo que aplica el habla de Perro añadiendo el guau
        
        cadena= "Soy un " + nombreClase + " " + super().__str__()
        
        return cadena
   
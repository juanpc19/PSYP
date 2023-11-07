class Libro:
    
    def __init__(self, titulo, autor, numeroEjemplares, numeroEjemplaresPrestados):
        self.titulo=titulo
        self.autor=autor
        self.numeroEjemplares=numeroEjemplares
        self.numeroEjemplaresPrestados=numeroEjemplaresPrestados
    
    def prestamo(self):
        resultado=False
        if self.numeroEjemplaresPrestados<self.numeroEjemplares:
            self.numeroEjemplaresPrestados+=1
            resultado=True

        return resultado
    
    def devolucion(self):
        resultado=False
        if self.numeroEjemplaresPrestados>0:
            self.numeroEjemplaresPrestados-=1
            resultado=True

        return resultado
        
    def __str__(self):
        cadena = "Titulo: " + self.titulo + "\n"
        cadena += "Autor: " + self.autor + "\n"
        cadena += "Numero ejemplares: " + str(self.numeroEjemplares) + "\n"
        cadena += "Numero ejemplares prestados: " + str(self.numeroEjemplaresPrestados)
        return cadena
            
    def __eq__(self, objeto):
        iguales=False
        if self.titulo==objeto.titulo and self.autor==objeto.autor:
            iguales=True
            
        return iguales
    
    def __lt__(self, objeto):
        menor=False
        if self.autor<objeto.autor:
            menor=True
            
        return menor
    


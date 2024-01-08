from threading import Thread

class CuentaVocales(Thread):
    def __init__(self,vocal):
        Thread.__init__(self)
        self.vocal=vocal
        
    def run(self):
    
        fichero="Tema3ProgDeHilos/ejerciciosParte1/ej4/vocales.txt"
        
        contador=0
        
        try:
            with open(fichero, 'r') as f:
                    #vuelco archivo en string texto
                    texto=f.read()
                    #cuento ocurrencias de vocal en texto y las asigno a contador
                    contador=texto.count(self.vocal)
                    #devuelvo contador
            print(self.vocal, ": ", contador)
            
                    
        except FileNotFoundError:   
            print("File not found!")
        except Exception as e:
            print("An error occurred:", e)
        
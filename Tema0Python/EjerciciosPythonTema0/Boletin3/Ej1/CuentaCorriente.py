class CuentaCorriente:
    
    ##con 2 cuentas me vale para los metosdos especiales
  
    
    
    def __init__(self, dni, saldo):
        self.dni=dni
        self.nombre=""
        self.saldo=saldo
        
    def __init__(self, dni ,nombre, saldo):
        self.dni=dni
        self.nombre=nombre
        self.saldo=saldo
        
    def ingresarDinero (self, dni, saldo):
        self.dni=dni
        self.saldo+=saldo
        
    def sacarDinero (self, dni, saldo):
        self.dni=dni
        if (self.saldo>=saldo):
            self.saldo-=saldo
            
    def __str__(self):
        cadena = "DNI: " + self.dni + "\n"
        cadena += "Nombre: " + self.nombre + "\n"
        cadena += "Saldo: " + str(self.saldo)
        return cadena
            
    def __eq__(self, objeto):
        iguales=False
        if self.dni==objeto.dni:
            iguales=True
            
        return iguales
    
    def __lt__(self, objeto):
        menor=False
        if self.dni<objeto.dni:
            menor=True
            
        return menor
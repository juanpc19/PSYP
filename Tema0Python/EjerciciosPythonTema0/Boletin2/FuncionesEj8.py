class FuncionesEj8:
    
   #print de menu
    def menu(self):
        
        print("""
              Libreta de direcciones:
               1. Agregar venta.
               2. Total de ventas de un producto."""
               )
    #si el producto  no esta en la lista lo agrega con valor de cantidadVendida si si esta en la lista 
    # le suma cantidadVendida a producto ya existente y luego devuelvo lista en return
    def agregarVenta(self, producto, cantidadVendida, listaVentas):
        
        if producto not in listaVentas:
            listaVentas[producto]=cantidadVendida
            print("Venta agregada.")
       
        else:
            listaVentas[producto]+=cantidadVendida
            print("Venta agregada.")
            
        return listaVentas
    
    #si el producto esta en la lista extraigo valor del producto especificado 
    # y lo asigno a totalVentas que devuelvo en return de lo contrario hago print indicando que no esta   
    def cuentaVentas(self, producto, listaVentas):
        totalVentas=0
        
        if producto in listaVentas:
            totalVentas=listaVentas[producto]
        else:
            print("No se ha vendido ese producto.")
        
        return totalVentas
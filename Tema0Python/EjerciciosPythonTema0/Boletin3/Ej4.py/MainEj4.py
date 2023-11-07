from Articulo import * 

art1=Articulo("lapiz",10.0,10)
art2=Articulo("goma",1.0,10)
art3=Articulo("goma",5.0,10)

print(art1.__str__())

pvp=art1.getPVP()
print("pvp:", pvp)
descuento=21
print()

pvpDescuento=art1.getPvpDescuento(pvp,descuento)
print("pvpDescuento:", pvpDescuento)
print()

art1.almacenar(10)
print("almacenar")
print(art1.__str__())
print()

art1.vender(1)
print("vender")
print(art1.__str__())
print()


print("iguales") if art2.__eq__(art3) else print ("no iguales")
print("iguales") if art1.__eq__(art2) else print ("no iguales")

print()

print("Primer articulo menor que segundo articulo.") if art1.__lt__(art2) else print ("Primer articulo no es menor que segundo articulo.")
print("Primer articulo menor que segundo articulo.") if art2.__lt__(art1) else print ("Primer articulo no es menor que segundo articulo.")


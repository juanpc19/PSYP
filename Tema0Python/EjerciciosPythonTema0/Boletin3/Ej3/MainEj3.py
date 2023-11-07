from Punto import*

pt1=Punto(1,1)

pt2=Punto(5,0)

print(pt1.__str__())

pt1.setXY(-5,1)
print(pt1.__str__())

pt1.desplaza(1,-1)

print("coordenadas:")
print(pt1.__str__())
print(pt2.__str__())


distancia=pt2.distancia(pt1)    
print(distancia)




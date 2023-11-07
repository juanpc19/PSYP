from Empleado import*
from Operario import*
from Directivo import*
from Oficial import*
from Tecnico import*

emp1=Empleado("pepe")

print(emp1.__str__())

dir1=Directivo("paxi")

print(dir1.__str__())

ope1=Operario("paco")

print(ope1.__str__())

ofi1=Oficial("manu")

print(ofi1.__str__())

tec1=Tecnico("tony")

print(tec1.__str__())
#declaro variables 
numeroIntroducido=int (input("Introduzca numero para establecer base y altura del triangulo:"))

cadena=""

#metodo1
for contador in range (1,numeroIntroducido+1):
    #print de espacio tantas veces como numerointroducido-contador concatenado a print de asterisco y espacio tantas veces como contador
    print(" "*(numeroIntroducido-contador)+"* "*contador)
    
#metodo2
for contador in range (1,numeroIntroducido+1):
    cadena+=" "*(numeroIntroducido-contador)
    cadena+="* "*contador
    cadena+="\n"
print(cadena)


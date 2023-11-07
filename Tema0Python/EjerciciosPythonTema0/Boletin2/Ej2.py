#Creo lista vacia
lista=[]

#solicito 10 numero para rellenarla con append
for contador in range(0,10):
    numero=int (input("Introduzca un numero entero: "))
    lista.append(numero)

#igualo minimo a min de lista por probar almacenando en variable y sin almacenar el maximo
numeroMin=min(lista)
#print de max y min sin y con variable usando el max lista directamente
print("Numero maximo:", max(lista), "numero minimo:", numeroMin)

################################################################################################

#Creo lista vacia
lista=[]
numeroMax=0
numeroMin=100

#solicito 10 numero para rellenarla con append
for contador in range(0,10):
    numero=int (input("Introduzca un numero entero: "))
    lista.append(numero)
    
#recorro lista manualmente modificando valores de min y max si corresponde
for contador in range(0,10):
    
    if lista[contador]<=numeroMin:
        numeroMin=lista[contador]
        
    if lista[contador]>=numeroMax:
        numeroMax=lista[contador]  
        
#hago print de min y max       
print ("Maximo:", numeroMax, "minimo:", numeroMin)




    
    


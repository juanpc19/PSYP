#creo diccionario con codigo de encriptacion
diccionario = { "e": "p", "i": "v","k": "i", "m": "u", "p": "m", "q": "t", "r": "e", "s": "r", "t": "k","u": "q", "v": "s"}

#solicito la frase 
frase=input("introduzca una frase a encriptar:")
#paso la cadena a lista de cadenas para poder modificar frase segun posicion
listaPalabrasFrase=list(frase)

#recorro diciconario a traves de claves 
for clave in diccionario:
    #si la clave actual esta en la frase 
    if clave in frase:
        #extraigo la posicion de esta con index
        posicion=frase.index(clave)
        #y cambio valor de listaPalabrasFrase en posicion por valor de clave llevando asi a cabo la encriptacion
        listaPalabrasFrase[posicion]=diccionario[clave]
      
#reinicio la cadena para reutilizar variable
frase=""

#recorro lista cadenas 
for letra in listaPalabrasFrase:
    #extrayendo las letras y añadiendolas a frase
    frase+=letra
#hago print de frase ya codificada
print(frase)
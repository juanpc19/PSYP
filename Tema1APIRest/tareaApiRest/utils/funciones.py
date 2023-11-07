
from flask import*

#modificadas con nombreFichero como parametro entrada

#funcion que guarda abre nombreFichero en modo lectura guardando esta lectura en archivo lo cual me permite leer o modificar el archivo desde python, 
# carga el objeto creado (archivo) en tiendas en formato json,
# cierra el archivo y devuelve el contenido del mismo que ahora esta en tiendas en el return
def leerFichero(nombreFichero):
    archivo = open(nombreFichero, "r") 
    tiendas = json.load(archivo)
    archivo.close()
    return tiendas


#funcion que recibe un diccionario abre nombreFichero en modo escritura guardando esta escritura en archivo lo cual me permite leer o modificar el archivo desde python,
# sobreescribe el objeto creado (archivo) con los valores de tiendas (el diccionario con valor/valores de turno) y cierra el archivo
def escribeFichero(nombreFichero, tiendas):
    archivo = open(nombreFichero, "w")
    json.dump(tiendas,archivo)
    archivo.close()
    
    

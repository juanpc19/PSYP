from threading import Timer


def saludo(mensaje):
    print(mensaje)


if __name__ == "__main__":
    temporizador = Timer(5, saludo, ("Hola a todos",))#segundos de time, funcion a ejecutar, datos que requiera la funcion
    temporizador.start()#espera tiempo definido y luego ejecuta la funcion
    print("Esperando a que se ejecute la función")
    temporizador.cancel()#esto cancela la cuenta atras de lo contrario print en 5 segundos
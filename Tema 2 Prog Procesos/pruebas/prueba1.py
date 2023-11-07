from multiprocessing import *
def hello(name):
    print("helloo", name)
    #name parametro entrada en p= es "elena" como simulacion input.
    
if __name__ == "__main__":
    p=Process(target=hello, args=("Elena",))
    #start para comenzar proceso especificado
    p.start()
    #join para ejecutar primero el que añado con join y despues el de abajo (sobreescribe prioridad)
    p.join()
    print("fin main")
    
    
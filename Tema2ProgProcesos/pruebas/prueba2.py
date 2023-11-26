from multiprocessing import*
import time

def suma (num1,num2):
    res=num1+num2
    print("suma igual a:", res)
    
def hello(name):
    print("helloo", name)
    #name parametro entrada en p= es "elena" como simulacion input
    
if __name__ == "__main__":
    inicio=time.time()
    p1=Process(target=suma, args=(3,5))
    p2=Process(target=hello, args=("paxi",))
    #empieza primero asi qu es main
    p1.start()
    #empieza segundo
    p2.start()
    #main espera a primero
    p1.join()
    #
    p2.join()
    
    fin=time.time()
    print ("tiempo", fin-inicio)
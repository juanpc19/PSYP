from multiprocessing import Pipe, Process
import random
from time import *

def generadorIps(a1):
    
    #lista para guardar ips
    listaIps=[]
    #bucle 10 iteraciones
    for i in range(10):
        # genero partes de la ip 
        segmento1 = random.randint(0, 255)
        segmento2 = random.randint(0, 255)
        segmento3 = random.randint(0, 255)
        segmento4 = random.randint(0, 255)

        # junto las partes de la ip con puntos
        ip = f"{segmento1}.{segmento2}.{segmento3}.{segmento4}"
        #las voy guardando en lista
        listaIps.append(ip)
        
    #envio la lista al siguiente proceso al salir de bucle
    a1.send(listaIps)
    #cierro extremo conducto
    a1.close()


def filtraIps(b1,b2):
    #lista para guardar ips una vez filtradas
    listaIpsFiltrada=[]
    #lista axuiliar usada para recibir la lista de 10 ips
    listaAuxiliar=b1.recv()
    
    #recorro lista auxiliar de 10 ips
    for ip in listaAuxiliar:
        #segmento la ip en partes en el punto
        segmentos=ip.split(".")
        #filtro ips comprobando primer segmento menor a 223 por lo que es clase a,b o c
        if int(segmentos[0])<=223:
            #si lo es la añado a la lista filtrada
            listaIpsFiltrada.append(ip)
            
    #paso lista ips filtrada a siguiente proceso al salir de bucle
    b2.send(listaIpsFiltrada)        
    
    #cierro extremos de conductos
    b1.close()
    b2.close()
            
def cosa(c1):
    #recibo listra filtrada
    listaIpsFiltrada=c1.recv()
    
    #la recorro 
    for ip in listaIpsFiltrada:
        #segmento ip en partes a partir de punto
        segmentos=ip.split(".")
        
        #hago print de ip y su tipo segun primer segmento
        if int(segmentos[0]) <= 126:
            print(segmentos, "Clase A") 
        elif int(segmentos[0]) <= 191:
            print(segmentos, "Clase B") 
        elif int(segmentos[0]) <= 223:
            print(segmentos, "Clase C") 
            
    #cierro extremo conducto al leer todas las ips
    c1.close()
    
if __name__ == "__main__":
    
    #creo tuberias
    a1,b1=Pipe()
    b2,c1=Pipe()
    
    #asigno extremos a procesos
    p1=Process(target=generadorIps, args=(a1,))
    p2=Process(target=filtraIps, args=(b1,b2))
    p3=Process(target=cosa, args=(c1,))

    #inicio procesos y dejo que finalicen a su ritmo
    inicio=time()
    p1.start()
    final=time()
    
    inicio2=time()
    p2.start()
    final2=time()
    
    inicio3=time()
    p3.start()
    final3=time()

    print(final-inicio)
    
    print(final2-inicio2)
    
    print(final3-inicio3)
         

from multiprocessing import Pipe, Process
import random
from time import *

#Genera las ips
def generadorIps(a1):
    #bucle 10 iteraciones para 10 ips
    for _ in range(10):
        # genero partes de la ip 
        segmento1 = random.randint(0, 255)
        segmento2 = random.randint(0, 255)
        segmento3 = random.randint(0, 255)
        segmento4 = random.randint(0, 255)
        # junto las partes de la ip con puntos
        ip = f"{segmento1}.{segmento2}.{segmento3}.{segmento4}"
        #una vez generada la envio por pipe
        a1.send(ip)
    #una vez enviadas las 10 ips envio none
    a1.send(None)    
    #cierro extremo conducto
    a1.close()

#filtra las ips eliminando las de clase D
def filtraIps(b1,b2):

    #recibe ip por pipe
    ip=b1.recv()
    #mientras ip no sea none
    while ip is not None:
        #segmento la ip en partes en el punto
        segmentos=ip.split(".")
        #filtro ip comprobando primer segmento menor a 223 por lo que es clase a,b o c
        if int(segmentos[0])<=223:
            #si no es clase d la envio por pipe
            b2.send(ip)     
        #recibo siguiente ip
        ip=b1.recv()
    #una vez recibo none no quedan ips por lo que envio none al siguiente extremo de pipe
    b2.send(None)
    
    #cierro extremos de conductos
    b1.close()
    b2.close()
            
#hace print de ips recibidas junto a string tipo ip
def cosa(c1):
    #recibo ip 
    ip=c1.recv()
    #mientras ip no sea none
    while ip is not None:
        #segmento ip en partes a partir de punto
        segmentos=ip.split(".")
        #hago print de ip y su tipo segun primer segmento
        if int(segmentos[0]) <= 126:
            print(segmentos, "Clase A") 
        elif int(segmentos[0]) <= 191:
            print(segmentos, "Clase B") 
        elif int(segmentos[0]) <= 223:
            print(segmentos, "Clase C") 
        #recibo siguiente ip 
        ip=c1.recv()        
        
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
         

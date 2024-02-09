

import random
from threading import Barrier, Condition
import time
from carrera import Carrera


if __name__=="__main__":
    
    barrera=Barrier(10)
    cond=Condition()
   
    hilos=[]
    
    for i in range (10):
        hilo=Carrera(str(i), barrera, cond)
        hilo.start()
        time.sleep(random.randint(1,2))#para ralentizar ejecucion hilos y ver funcionamiento mejor
        hilos.append(hilo)
        
    for h in hilos:
        h.join()
        
        
#problemas con timer comun, si timer propio el hilo se inicia dos veces 1 con run en main y otra con timer .
#hago delay con timesleep porque si hago timer propio pa lanzar hilo solo sirve para ponerse en linea salida no para salir, 
# una vez esta en linea salida el hilo ya ha empezado y no puedo hacerle otro start con timer,
# y la rotura de la barrera se da sola al llegar los 10 hilos por lo que no puedo pararla durante 3 segundos o romperla a los 3 segundos
#el timer no es buena idea porque reinicia el proceso y explota

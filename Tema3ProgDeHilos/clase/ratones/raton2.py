from threading import Thread
import time

#metodo sin herencia no usar
def comer (nombre,tiempoAlimentacion):
    print("el raton", nombre, "empieza a comer")
    time.sleep(tiempoAlimentacion)#"delay"
    print("el raton", nombre, "ha termindao de comer")
    
if __name__=="__main__":
    r1=Thread(target=comer,args=("mini",1))
    r2=Thread(target=comer,args=("mani",3))
    r3=Thread(target=comer,args=("moe",2))
    
    
    r1.start()
    r2.start()
    r3.start()
from queue import Queue
from threading import Condition
from productor import Productor
from consumidor import Consumidor

if __name__=="__main__":
    cond = Condition()
    cola = Queue()
    
    prod =Productor("prod")
    cons=Consumidor("")
   
    cons.start()
    prod.start()
    
    
 
    
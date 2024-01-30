from queue import Queue
from threading import Condition
from productor import Productor
from consumidor import Consumidor

if __name__ == "__main__":
    cola = Queue(1)
    cond = Condition()

    prod = Productor("prod", cola, cond)
    cons = Consumidor("cons", cola, cond)
    
    cons.start()
    prod.start()
 
    
from multiprocessing import Process, Queue

#crea proceso y lo pone en cola
def productor(cola):
    for i in range(1,11):
        cola.put(i)
    cola.put(None)

#saca un proceso de la cola
def consumidor(cola):
    objeto=cola.get()
    while objeto is not None:
        print(objeto)
        objeto=cola.get()

if __name__=="__main__":
    cola=Queue()
    
    p1 = Process(target=productor, args=(cola,))
    p2 = Process(target=consumidor, args=(cola,))
    
    p1.start()
    p2.start()
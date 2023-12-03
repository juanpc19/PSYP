import random
from multiprocessing import Pool

#genera 6 float random entre 1 y 10 y los guarda en fichero cuya ruta se da como param entrada 
def CrearNotasAlumno(FicheroNotasAlumno):
    
    try:
        with open(FicheroNotasAlumno, "w") as notasAlumno:
            for _ in range(6):
                numero=random.uniform(0,10)
                notasAlumno.write (str(numero))
                notasAlumno.write("\n")
            
    except FileNotFoundError:   
        print("Archivo no encontrado.")
    except Exception as e:
        print("El siguiente error ha ocurrido:", e)
    
#recibe lista de rutas de ficheros y lista de nombres, saca media de cada fichero y le añade siguiente nombre en lista nombres
def LeerNotasAlumnos(nombreAlumno,FicheroNotasAlumno):
    sumaTotal=0.0
    notaMedia=0.0
    try:
        medias=open("Tema2ProgProcesos\\ejercicios\\ficheros\\ej3\\medias.txt", "a", encoding="utf8")
        with open(FicheroNotasAlumno, "r") as notasAlumno:
        
            for linea in notasAlumno.readlines():
                sumaTotal+=float(linea)
            notaMedia=sumaTotal/6
            medias.write(f"{notaMedia} : {nombreAlumno}\n")
            
    except FileNotFoundError:   
        print("Archivo no encontrado.")
    except Exception as e:
        print("El siguiente error ha ocurrido:", e)       
             
#Lee archivo medias y obtiene nota maxima y la imprime, necesita 2 procesos anteriores finalizados,  p3 hace hace join ?
def maxNota():
    pass


# pipe mas lento que queue, queue construido sobre base pipe, pipe para 2 procesos a la vez, queue para tantos como quiera (3 por ejemplo)
if __name__=="__main__":
    #nombres de los alumnos
    nombresAlumnos= ["María","Alejandro","Lucía","Pablo","Marta","Javier","Ana","Carlos","Sofía","Diego"]
    #lista rutas notasAlumnos
    FicherosNotasAlumnos = []
    #for crea 10 rutas para ficheros y las guarda en lista
    for i in range(1, 11):
        ruta = f"Tema2ProgProcesos\\ejercicios\\ficheros\\ej3\\Alumno{i}.txt"
        FicherosNotasAlumnos.append(ruta)
     
    #Crea una lista de elementos tipo tupla, cada una contiene 2 datos
    nombresNotasAlumnos = [(nombre, ruta) for nombre, ruta in zip(nombresAlumnos, FicherosNotasAlumnos)]
    
    with Pool(processes=10) as pool:
        #pool de proceso 1 le paso fichero para que guarde 6 notas
        resultado=pool.map(CrearNotasAlumno,FicherosNotasAlumnos)
        pool.close()
        pool.join()
        
    with Pool(processes=10) as pool2:
        #pool de proceso 2 le paso conjunto de 10 rutas de ficheros (FicherosNotasAlumno) y 10 nombres de alumnos (nombresAlumnos) en una lista de tuplas
        resultado2=pool2.starmap(LeerNotasAlumnos,nombresNotasAlumnos)
        
        
#los procesos tipo 1 y tipo 2 deben ser dependientes o independientes? modificar de 1 a 2 pool para ello? con 1 y con 2 pool sigue saltandose nombres
        
    
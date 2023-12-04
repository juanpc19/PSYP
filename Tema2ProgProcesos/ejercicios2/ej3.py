import random
from multiprocessing import Pool,Process

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
            medias.write(f"{notaMedia} {nombreAlumno}\n")
            
    except FileNotFoundError:   
        print("Archivo no encontrado.")
    except Exception as e:
        print("El siguiente error ha ocurrido:", e)       
             
#Lee archivo medias y obtiene nota maxima y la imprime, necesita 2 procesos anteriores finalizados,  p3 hace hace join ?
def maxNota(fichero):
    #Lee el fichero medias.txt. En cada línea del fichero aparecerá una nota, un espacio y el nombre del alumno. 
    # Este proceso debe leer el fichero y obtener la nota máxima. 
    # Imprimirá por pantalla la nota máxima junto con el nombre del alumno que la ha obtenido.
    try:
        with open(fichero, "r") as medias:
            max=0.0
            mejorAlumno=""
            for linea in medias.readlines():
                listaNotasAlumnos=linea.split(" ")
                if float(listaNotasAlumnos[0])>max:
                    max=float(listaNotasAlumnos[0])
                    mejorAlumno=linea    
            print(mejorAlumno)
            
  
    except FileNotFoundError:   
        print("Archivo no encontrado.")
    except Exception as e:
        print("El siguiente error ha ocurrido:", e)   
    
    
# pipe mas lento que queue, queue construido sobre base pipe, pipe para 2 procesos a la vez, queue para tantos como quiera (3 por ejemplo)
if __name__=="__main__":
    
    #nombres de los alumnos
    nombresAlumnos= ["María","Alejandro","Lucía","Pablo","Marta","Javier","Ana","Carlos","Sofía","Diego"]
    
    #lista rutas notasAlumnos
    FicherosNotasAlumnos = []

    #fichero de las medias
    ficheroMedias="Tema2ProgProcesos\\ejercicios\\ficheros\\ej3\\medias.txt"
    
    #for crea 10 rutas para ficheros y las guarda en lista
    for i in range(1, 11):
        ruta = f"Tema2ProgProcesos\\ejercicios\\ficheros\\ej3\\Alumno{i}.txt"
        FicherosNotasAlumnos.append(ruta)
     
    #Crea una lista de elementos tipo tupla, cada una contiene 2 datos
    nombresNotasAlumnos = [(nombre, ruta) for nombre, ruta in zip(nombresAlumnos, FicherosNotasAlumnos)]
    
    with Pool(processes=10) as pool:
        #pool de proceso 1 le paso fichero para que guarde 6 notas
        resultado=pool.map(CrearNotasAlumno,FicherosNotasAlumnos)
    #hago que main espere a pool
    pool.join()
    
    with Pool(processes=10) as pool2:
        #pool de proceso 2 le paso conjunto de 10 rutas de ficheros (FicherosNotasAlumno) y 10 nombres de alumnos (nombresAlumnos) en una lista de tuplas
        resultado2=pool2.starmap(LeerNotasAlumnos,nombresNotasAlumnos)
    #hago que main espere a pool2
    pool2.join()
    p3=Process(target=maxNota, args=(ficheroMedias,))

    #empiezo el 3 cuando joins de 1 y 2 acaben
    p3.start()
    
        
       
       
        
        
        




#j
    
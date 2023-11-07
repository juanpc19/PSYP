
from app import app
#esto para ejecutar como antes

#si cumple es fichero main y ejecuta el main, esto debe estar al final del archivo no se porque
if __name__== "__main__":
    #debug modo desarrollo on/true, host por defecto, port el que quieras
    app.run(debug=True, host="0.0.0.0", port=5050)
    
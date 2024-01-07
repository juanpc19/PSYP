
from flask import Flask

from personas.routes import personasBP
    
app=Flask(__name__)


app.register_blueprint(personasBP, url_prefix="/personas")





#si cumple es fichero main y ejecuta el main, esto debe estar al final del archivo no se porque
if __name__== "__main__":
    #debug modo desarrollo on/true, host por defecto, port el que quieras
    app.run(debug=True, host="0.0.0.0", port=5050)

import secrets
from flask import Flask
from flask_jwt_extended import JWTManager

from personas.routes import personasBP
from departamentos.routes import departamentosBP
from users.routes import usersBP

app=Flask(__name__)

app.register_blueprint(personasBP, url_prefix="/personas")
app.register_blueprint(departamentosBP, url_prefix="/departamentos")
app.register_blueprint(usersBP, url_prefix="/users")


app.config["SECRET_KEY"]=secrets.token_hex(16)
jwt=JWTManager(app)

#si cumple es fichero main y ejecuta el main, esto debe estar al final del archivo no se porque
if __name__== "__main__":
    #debug modo desarrollo on/true, host por defecto, port el que quieras
    app.run(debug=True, host="0.0.0.0", port=5050)

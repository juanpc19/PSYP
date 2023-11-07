
import random # para pass random
from flask import Flask
from .tiendas.routes import tiendasBP
from .empleados.routes import empleadosBP
from .users.routes import usersBP

from flask import Flask
from flask_jwt_extended import JWTManager

#Creo la app tipo flask
app = Flask(__name__)

#investigar string aleatoria para pass
app.config['SECRET_KEY']='contraseña'
jwt=JWTManager(app)

#registro en la app  las blueprints con un end point predeterminado parano usarlo en cada metodo
app.register_blueprint(tiendasBP, url_prefix='/tiendas')
app.register_blueprint(empleadosBP, url_prefix='/empleados')
app.register_blueprint(usersBP, url_prefix='/users')

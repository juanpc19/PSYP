from utils.funciones import leerFichero, escribeFichero

from flask import Blueprint, request

import bcrypt

from flask_jwt_extended import create_access_token

ficheroUsers="Tema1APIRest/tareaApiRest/ficheros/users.json"

usersBP=Blueprint('users',__name__)

@usersBP.post("/")
def registrarUsuario():
    users=leerFichero(ficheroUsers)
    
    if request.is_json:
        
        user=request.get_json()
        
        password= user ['password'].encode('utf-8')
        
        salt = bcrypt.gensalt()
        
        hashPassword=bcrypt.hashpw(password,salt).hex()
        
        user['password']=hashPassword
        
        users.append(user)
        
        escribeFichero(ficheroUsers, users)
        
        token=create_access_token(identity=user['username'])
        
        return {'token': token}, 201
    
    return {"error": "Request must be JSON"}, 415

@usersBP.get('/')
def loginUser():
    users=leerFichero(ficheroUsers)
    if request.is_json:
        user=request.get_json()
        username=user['username']
        password=user['password'].encode('utf-8')
        
        for userFile in users:
            if userFile['username']==username:
                passwordFile=userFile['password']
                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token=create_access_token(identity=username)
                    return {'token': token}, 200
                else:
                    
                    return {'error': 'No authorized'}, 401
        return {'error': 'User not found'}, 404
    return {'error': 'request must be JSON '}, 415
            
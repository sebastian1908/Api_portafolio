from conexion.Conexion import Database as conn
from decorador.response import Response as r
from model.usuarios_model import Usuarios as usu_model
from model.codigo_recuperacion_model import RecuperarPass
from datetime import datetime, timedelta
from dotenv import load_dotenv
import bcrypt
import json
import jwt
import os 
import resend
import random

load_dotenv()

class Usuarios:

    def __init__(self):
        self.db = conn().setConnection()
    
    def login(self, data):
        key = os.getenv("SECRET_KEY")
        response = r()
        usuario = data["usuario"]
        passw = data["password"]

        query = self.db.query(usu_model).filter(usu_model.USUARIO == usuario, usu_model.ACTIVO == 1).first()

        if query and bcrypt.checkpw(passw.encode('utf-8'), query.PASS.encode('utf-8')):
            payload = {
                'usuario': usuario,
                'exp': datetime.utcnow() + timedelta(hours=1)
            }
            token = jwt.encode(payload, key, algorithm='HS256')
            return response.success(token)
        else:
            response = {
                "statusCode": 400,
                "body": json.dumps({
                    "error": True,
                    "message": "Usuario o contraseña incorrecto."
                })
            }
            return response
        

    def create_user(self, data):
        response = r()
        nombre = data["nombre"]
        apellido = data["apellido"]
        usuario = data["usuario"]
        passw = data["password"]
        dataPass = passw.encode('utf-8')
        hashed = bcrypt.hashpw(dataPass, bcrypt.gensalt())

        query = usu_model(NOMBRE=nombre, APELLIDO=apellido, USUARIO=usuario, PASS=hashed)

        if query:
            self.db.add(query)
            self.db.commit()
            return response.created(query)
        else:
            return response.bad_request(query)
        
    
    def recove_password(self, data):
        response = r()
        usuario = data["usuario"]
        query = self.db.query(usu_model).filter(usu_model.USUARIO == usuario, usu_model.ACTIVO == 1).first()

        if query:
            payload = {
                "id": query.ID
            }
            recup_pass = self.mail(payload)
            return r.code_recove(self, recup_pass)
        else:
            response = {
                "statusCode": 404,
                "body": json.dumps({
                    "error": True,
                    "message": "El usuario no existe."
                })
            }
            return response
    
    def mail(self, data):
        resp = r()
        load_dotenv()
        key = os.getenv("API_KEY_MAIL")
        codigo_recuperacion = random.randint(10000, 99999)
        id_user = data["id"]

        resend.api_key = key
        re = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "*************************",
            "subject": "RECUPERAR CONTRASEÑA",
            "html": f"<div style='font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; max-width: 600px; margin: 0 auto; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);'><p style='color: #555555;'>SU CODIGO DE RECUPERACION ES : <strong style='color: #d9534f;'>{codigo_recuperacion}</strong></p><a href='' style='display: inline-block; padding: 10px 20px; margin-top: 20px; background-color: #5cb85c; color: #ffffff; text-decoration: none; border-radius: 5px;'>Visita la página</a></div>"
        })
        
        query = self.db.query(RecuperarPass).filter_by(ID_USUARIO=id_user).first()

        if query:
            query.CODIGO = codigo_recuperacion
        else:
            query = RecuperarPass(CODIGO=codigo_recuperacion, ID_USUARIO=id_user)
            self.db.add(query)

        self.db.commit()
        return resp.success(re)

    def new_pass(self, data):
        resp = r()
        codigo_recp = data["codigo"]
        nueva_pass = data["nueva_password"]
        dataPass = nueva_pass.encode('utf-8')
        hashed = bcrypt.hashpw(dataPass, bcrypt.gensalt())

        recuperacion = (
            self.db.query(RecuperarPass)
            .join(usu_model, usu_model.ID == RecuperarPass.ID_USUARIO)
            .filter(RecuperarPass.CODIGO == codigo_recp, RecuperarPass.ACTIVO == 1)
            .first()
        )

        if recuperacion:
            
            usuario = (
                self.db.query(usu_model)
                .filter_by(ID=recuperacion.ID_USUARIO)
                .first()
            )

            if usuario:
                usuario.PASS = hashed
                self.db.commit()
                return resp.created(usuario)
            else:
                response = {
                    "statusCode": 404,
                    "body": json.dumps({
                        "error": True,
                        "message": "Usuario no encontrado."
                    })
                }
                return response
        else:

            response = {
                "statusCode": 500,
                "body": json.dumps({
                    "error": True,
                    "message": "Error, ocurrió un fallo."
                })
            }
            return response
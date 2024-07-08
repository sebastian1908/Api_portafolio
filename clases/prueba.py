from conexion.Conexion import Database
from model.prueba_model import Prueba as Prueba_model
from decorador.response import Response as r
import resend
import os 
from dotenv import load_dotenv

"""
ARCHIVO USADO PARA PRUEBAS
"""


class Probando:

    def testData(self):
        db = Database().setConnection()
        resp = r()
        consulta = db.query(Prueba_model).all()
        response = []

        if consulta:
            for char in consulta:
                result = {
                    "id": char.id,
                    "nombre": char.nombre
                }
                response.append(result)

            return resp.success(response)
        else:
            return resp.no_content(response)
    
    def insertData(self, data):
        db = Database().setConnection()
        resp = r()
        name = data["nombre"]
        query = Prueba_model(nombre=name)

        if query:
            db.add(query)
            db.commit()
            return resp.created(query)
        else:
            return resp.bad_request(query)


    def updatetData(self, data):
        db = Database().setConnection()
        resp = r()
        id_value = data["id"]
        name = data["nombre"]

        query = db.query(Prueba_model).filter_by(id=id_value).first()
        if query:
            query.nombre = name
            db.commit()
            return resp.success(int(query.id))
        else:
            return resp.bad_request(query)

    def deletetData(self, data):
        db = Database().setConnection()
        resp = r()
        id_value = data["id"]

        query = db.query(Prueba_model).filter_by(id=id_value).first()
        if query:
            db.delete(query)
            db.commit()
            return resp.success(query.id)
        else:
            return resp.bad_request(query)

    def mail(self):
        resp = r()
        load_dotenv()
        key = os.getenv("API_KEY_MAIL")
        resend.api_key = key
        re = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "***********************",
            "subject": "Cara de rata",
            "html": "<p>La propia callita <strong>VISITA LA PAGINA WEB CALLITA.CIM</strong>!</p>"
        })

        return resp.success(re)

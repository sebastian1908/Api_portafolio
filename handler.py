import json
from decorador.excepciones import Exepciones
from clases.usuarios import Usuarios
from clases.prueba import Probando

excepciones = Exepciones()

@excepciones.capture_exception(require_token=False)
def login(event, context):
    body = event["body"]
    datos = json.loads(body)
    user = Usuarios()
    response = user.login(datos)
    return response

@excepciones.capture_exception
def create_user(event, context):
    body = event["body"]
    datos = json.loads(body)
    user = Usuarios()
    response = user.create_user(datos)
    return response

@excepciones.capture_exception
def hello(event, context):
    pru = Probando()
    pruData = pru.testData()
    print(pruData)
    return pruData

def recove_password(event, context):
    body = event["body"]
    datos = json.loads(body)
    user = Usuarios()
    response = user.recove_password(datos)
    return response

def new_pass(event, context):
    body = event["body"]
    datos = json.loads(body)
    user = Usuarios()
    response = user.new_pass(datos)
    return response
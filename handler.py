import json
from decorador.excepciones import Exepciones
from clases.usuarios import Usuarios
from clases.prueba import Probando
from clases.noticias import Noticias

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

@excepciones.capture_exception
def recove_password(event, context):
    body = event["body"]
    datos = json.loads(body)
    user = Usuarios()
    response = user.recove_password(datos)
    return response

@excepciones.capture_exception
def new_pass(event, context):
    body = event["body"]
    datos = json.loads(body)
    user = Usuarios()
    response = user.new_pass(datos)
    return response

@excepciones.capture_exception
def noticie(event, context):
    body = event["body"]
    datos = json.loads(body)
    user = Noticias()
    user_id = event['user']["usuario"]
    response = user.create_notice(datos, user_id)
    return response

@excepciones.capture_exception
def insert_comment(event, context):
    body = event["body"]
    datos = json.loads(body)
    user = Noticias()
    user_id = event['user']["usuario"]
    response = user.create_comentario(datos, user_id)
    return response

@excepciones.capture_exception
def comentario_noticia(event, context):
    user = Noticias()
    user_id = event['user']["usuario"]
    response = user.ver_noticia(user_id)
    return response
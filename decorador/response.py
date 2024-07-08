import json
class Response:

    def success(self, funcion):
        
        response = {
            "statusCode": 200,
            "body": json.dumps({
            "error": False,
                "message": "Solicitud exitosa.",
                "data": funcion
            })
        }
    
        return response
    
    def created(self, funcion):

        response = {
            "statusCode": 201,
            "body": json.dumps({
            "error": False,
                "message": "Solicitud exitosa, datos creado con éxito."
            })
        }

        return response
    
    def code_recove(self, funcion):

        response = {
            "statusCode": 200,
            "body": json.dumps({
            "error": False,
                "message": "Codigo de recuperacion enviado con exito, revisa tu correo eletronico."
            })
        }

        return response
    

    def no_content(self, funcion):
        response = {
            "statusCode": 200,
            "body": json.dumps({
            "error": False,
                "message": "solicitud exitosa, no se encontro informacion."
            })
        }

        return response
    
    def bad_request(self, funcion):
        response = {
            "statusCode": 400,
            "body": json.dumps({
            "error": False,
                "message": "Error, algo fallo, vuelve a intentarlo."
            })
        }

        return response
    
    def token_expired(self, funcion):
        response = {
            "statusCode": 400,
            "body": json.dumps({
            "error": False,
                "message": "Error, token expired."
            })
        }

        return response
    
    def unauthorized(self, funcion):
        response = {
            "statusCode": 401,
            "body": json.dumps({
            "error": False,
                "message": "Error no tienes permiso para realizar esta accion."
            })
        }

        return response
    
        
    def forbidden(self, funcion):
        response = {
            "statusCode": 403,
            "body": json.dumps({
            "error": False,
                "message": "Error no estas autenticado."
            })
        }

        return response
    
    def not_found(self, funcion):
        response = {
            "statusCode": 404,
            "body": json.dumps({
            "error": False,
                "message": "Error no se encontro el recurso."
            })
        }

        return response
    
    def method_not_allowed(self, funcion):
        response = {
            "statusCode": 405,
            "body": json.dumps({
            "error": False,
                "message": "Error no se permite el uso de este metodo."
            })
        }

        return response
    
    def internal_server(self, funcion):
        response = {
            "statusCode": 500,
            "body": json.dumps({
            "error": False,
                "message": "Error de servidor."
            })
        }

        return response
    
    



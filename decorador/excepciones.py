from decorador.response import Response
import json
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

class Exepciones:
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY")

    def capture_exception(self, func=None, *, require_token=True):
        def decorator(func):
            def wrapper(event, context, *args, **kwargs):
                if require_token:
                    # Verificar el token JWT
                    try:
                        # Asegurarse de que el encabezado 'authorization' existe
                        if 'authorization' not in event['headers']:
                            raise KeyError('Authorization header missing')

                        token = event['headers']['authorization'].split()[1]
                        print(f"Token recibido: {token}")  # Imprimir el token recibido
                        payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
                        print(f"Token válido para el usuario: {payload['usuario']}")
                    except KeyError as e:
                        # Capturar el error si el encabezado no se encuentra
                        return {
                            'statusCode': 400,
                            'body': json.dumps({'message': f'Error: {str(e)}'})
                        }
                    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError) as e:
                        return {
                            'statusCode': 401,
                            'body': json.dumps({'message': 'Token no válido o expirado.'})
                        }

                # Capturar otras excepciones
                try:
                    return func(event, context, *args, **kwargs)
                except KeyError as k:
                    capture = self.error_key(k)
                    return capture
                except Exception as e:
                    print(f"Mensaje error --> {e}")
                    capture = Response.bad_request(self, func)
                    return capture

            return wrapper

        if func:
            return decorator(func)
        return decorator

    def error_key(self, k):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': f'Llave no encontrada: {k}'})
        }

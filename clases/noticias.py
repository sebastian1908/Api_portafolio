from conexion.Conexion import Database as conn
from decorador.excepciones import Exepciones as excep
from decorador.response import Response as r
from model.noticia_model import Noticias as noti_model
from model.usuarios_model import Usuarios
from model.comentario_model import Comentarios

class Noticias:
    def __init__(self):
        self.db = conn().setConnection()
        self.session = excep()

    def create_notice(self, data, usuario):
        db = conn().setConnection()
        resp = r()
        user = db.query(Usuarios.ROL).filter(Usuarios.USUARIO == usuario, Usuarios.ACTIVO == 1).first()
        
        if user:
            if user.ROL == 1:
                titulo = data.get("titulo")
                descrip = data.get("descripcion")

                if titulo and descrip:
                    query = noti_model(TITULO=titulo, DESCRIPCION=descrip)

                    db.add(query)
                    db.commit()
                    return resp.created(query)
                else:
                    return resp.bad_request("Título o descripción faltante")
            else:
                return resp.unauthorized("Usuario no autorizado para crear la noticia")
        else:
            return resp.unauthorized("Usuario no encontrado o inactivo")

        
    def create_comentario(Self, data, usuario):
        db = conn().setConnection()
        resp = r()
        user = db.query(Usuarios.ID ,Usuarios.ROL).filter(Usuarios.USUARIO == usuario, Usuarios.ACTIVO == 1).first()

        if user:
            if user.ROL == 1:
                comentario = data["comentario"]
                id_user = data["id_usuario"]

                if user.ID != id_user:
                    return resp.unauthorized("El usuario que intenta agregar el comentario, no es el mismo que esta logueado.")

                query = Comentarios(COMENTARIO=comentario, ID_USUARIO=id_user)

                if query:
                    db.add(query)
                    db.commit()
                    return resp.created(query)
            else:
                return resp.unauthorized("Usuario no autorizado para crear comentario")
        else:
            return resp.unauthorized("Usuario no encontrado o inactivo")
        

    def ver_noticia(self, usuario):
        resp = r()
        user = self.db.query(Usuarios.ID, Usuarios.ROL).filter(Usuarios.USUARIO == usuario, Usuarios.ACTIVO == 1).first()
        
        if user:
            if user.ROL == 1:
                id_user = self.db.query(Usuarios.ID).filter(Usuarios.USUARIO == usuario, Usuarios.ACTIVO == 1).first()
                valide_user = self.db.query(Usuarios.USUARIO, Usuarios.ROL).filter(Usuarios.ID == id_user[0], Usuarios.ACTIVO == 1).first()

                if valide_user[0] != usuario:
                    return resp.unauthorized("El usuario no tiene permiso.")

                query = ( 
                    self.db.query(noti_model, Comentarios, Usuarios)
                    .join(Comentarios, noti_model.ID == Comentarios.ID_NOTICIA)
                    .join(Usuarios, Comentarios.ID_USUARIO == Usuarios.ID)
                    .filter(noti_model.ACTIVO == 1, Usuarios.ID == id_user[0])
                    .all()
                )

                if not query:
                    return resp.no_content("No hay noticias disponibles.")

                response = []

                for i, j, u in query:
                    data = {
                        "ID": i.ID,
                        "TITULO": i.TITULO,
                        "DESCRIPCION": i.DESCRIPCION,
                        "FECHA_CREACION": str(i.FECHA_CREACION),
                        "USUARIO": u.USUARIO,
                        "COMENTARIO": j.COMENTARIO
                    }
                    response.append(data)
                
                return resp.success(response)
            else:
                return resp.no_content("No tienes ningún comentario.")
        else:
            return resp.unauthorized("Usuario no encontrado o inactivo.")

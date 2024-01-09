import psycopg
from models.connection import connectionSql 

class UsuarioAPI():

    conAux = connectionSql()
    conn = conAux.getConnection()

    def insertarUsuario(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "usuarios"(usuario,contraseña) VALUES (%(usuario)s, %(contrasena)s)
                        """, data)
        self.conn.commit()


    def usuarioEspecifico(self,id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "usuarios" WHERE id = %s
            """,(id,))

            return data.fetchone()    

    def usuarioEliminar(self,id):
        with self.conn.cursor() as cur :
            cur.execute("""
                DELETE FROM "usuarios" WHERE id = %s
        """,(id,))
            
        self.conn.commit()
    
    def usuarioActualizar(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "usuarios" SET usuario = %(usuario)s , contraseña = %(contrasena)s WHERE id = %(id)s
            """, data)
        self.conn.commit()

    

import psycopg
from models.connection import connectionSql 

class AutoresAPI():
    conAux = connectionSql()
    conn = conAux.getConnection()

    def TodosAutores(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
               select a.autor_id ,a.nombre,n.pais  from autores a join nacionalidades n on a.nacionalidad_id = n.nac_id order by 1
                        """, )
            
            return data.fetchall()

    # def insertarLibro(self,data):
    #     with self.conn.cursor() as cur:
    #         cur.execute("""
    #             INSERT INTO "libros"(titulo,autor_id,genero_id,anio_publicacion) 
    #                     VALUES (%(titulo)s, %(autor)s, %(genero)s, %(anio)s)
    #                     """, data)
    #     self.conn.commit()

    # def libroActualizar(self,data):
    #     with self.conn.cursor() as cur:
    #         cur.execute("""
    #             UPDATE "libros" 
    #                 SET titulo = %(titulo)s , 
    #                 autor_id = %(autor)s ,
    #                 genero_id = %(genero)s ,
    #                 anio_publicacion = %(anio)s 
    #                 WHERE libro_id = %(id)s
    #         """, data)
    #     self.conn.commit()
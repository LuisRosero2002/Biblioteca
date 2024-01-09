import psycopg
from models.connection import connectionSql 

class LibroAPI():
    conAux = connectionSql()
    conn = conAux.getConnection()

    def TodosLibros(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                select l.libro_id, l.titulo, a.nombre, g.genero, l.anio_publicacion  from "libros" l 
                join "autores" a on a.autor_id = l.autor_id 
                join "generos" g on g.genero_id = l.genero_id order by 1
                        """, )
            
            return data.fetchall()

    def insertarLibro(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "libros"(titulo,autor_id,genero_id,anio_publicacion) 
                        VALUES (%(titulo)s, %(autor)s, %(genero)s, %(anio)s)
                        """, data)
        self.conn.commit()

    def libroActualizar(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "libros" 
                    SET titulo = %(titulo)s , 
                    autor_id = %(autor)s ,
                    genero_id = %(genero)s ,
                    anio_publicacion = %(anio)s 
                    WHERE libro_id = %(id)s
            """, data)
        self.conn.commit()
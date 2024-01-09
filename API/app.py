from fastapi import FastAPI, Response, HTTPException
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from models.connection import connectionSql
from models.usuarios import UsuarioAPI
from models.libros import LibroAPI
from models.autores import AutoresAPI
from schema.user_schema import UsuariosSchema
from schema.libro_schema import LibroSchema 


app = FastAPI()
usuarioService = UsuarioAPI()
libroService = LibroAPI()
autoresServices = AutoresAPI()


@app.get("/", status_code=HTTP_200_OK)
def root():
    return {"Welcome":"Welcome to my API"}

class usuario():

    @app.get("/api/usuarios/{id}", status_code= HTTP_200_OK)
    def usuarioEspecifico(id:str):
        data = {}
        dataAux =  usuarioService.usuarioEspecifico(id)

        if(dataAux != None):
            data["id"] = dataAux[0]
            data["usuario"] = dataAux[1]
            data["contraseña"] = dataAux[2]
            return data

        raise HTTPException(status_code=HTTP_404_NOT_FOUND)

    @app.post("/api/usuarios",status_code= HTTP_201_CREATED)
    def usuarioInsertar(data_user:UsuariosSchema):
        data = data_user.dict()
        usuarioService.insertarUsuario(data)
        return Response(status_code= HTTP_201_CREATED)

    @app.delete("/api/usuario/borrar/{id}", status_code=HTTP_204_NO_CONTENT)
    def usuarioEliminar(id:str):
        usuarioService.usuarioEliminar(id)
        return Response(status_code=HTTP_204_NO_CONTENT)

    @app.put("/api/usuario/actualizar/{id}",status_code=HTTP_204_NO_CONTENT)
    def usuarioActualizar(data_user:UsuariosSchema, id:str):
        data = data_user.dict()
        data["id"]  = id
        usuarioService.usuarioActualizar(data)

class libros():

    @app.get("/api/libros", status_code= HTTP_200_OK)
    def libros():
        data = []
        dataAux =  libroService.TodosLibros()
        if(dataAux != None):

            for i,x in enumerate(dataAux):
                data.append({
                    "id":x[0],
                    "titulo":x[1],
                    "autor":x[2],
                    "genero":x[3],
                    "anio":x[4]
                })
            
            return data
        
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)

    @app.post("/api/libros/insertar",status_code= HTTP_201_CREATED)
    def libroInsertar(data_libro:LibroSchema):
        data = data_libro.dict()
        libroService.insertarLibro(data)
        return Response(status_code= HTTP_201_CREATED)

    # @app.delete("/api/usuario/borrar/{id}", status_code=HTTP_204_NO_CONTENT)
    # def usuarioEliminar(id:str):
    #     conn.usuarioEliminar(id)
    #     return Response(status_code=HTTP_204_NO_CONTENT)

    @app.put("/api/libro/actualizar/{id}",status_code=HTTP_204_NO_CONTENT)
    def usuarioActualizar(data_libro:LibroSchema, id:str):
        data = data_libro.dict()
        data["id"]  = id
        libroService.libroActualizar(data)


class Autores():

    @app.get("/api/autores", status_code= HTTP_200_OK)
    def autores():
        data = []
        dataAux =  autoresServices.TodosAutores()
        if(dataAux != None):

            for i,x in enumerate(dataAux):
                data.append({
                    "id":x[0],
                    "autor":x[1],
                    "pais":x[2]
                })
            print(data)
            return data
        
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)

    # @app.post("/api/libros/insertar",status_code= HTTP_201_CREATED)
    # def libroInsertar(data_libro:LibroSchema):
    #     data = data_libro.dict()
    #     libroService.insertarLibro(data)
    #     return Response(status_code= HTTP_201_CREATED)

    # # @app.delete("/api/usuario/borrar/{id}", status_code=HTTP_204_NO_CONTENT)
    # # def usuarioEliminar(id:str):
    # #     conn.usuarioEliminar(id)
    # #     return Response(status_code=HTTP_204_NO_CONTENT)

    # @app.put("/api/libro/actualizar/{id}",status_code=HTTP_204_NO_CONTENT)
    # def usuarioActualizar(data_libro:LibroSchema, id:str):
    #     data = data_libro.dict()
    #     data["id"]  = id
    #     libroService.libroActualizar(data)

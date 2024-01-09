import httpx

URLAPI = "http://127.0.0.1:8001"

class libroServiceAPI():
    url = URLAPI
    def getLibrosAPI(self):
        # parametros = {"parametro1": "valor1", "parametro2": "valor2"}
        # headers = {"Authorization": "Bearer tu_token"}
        self.url += "/api/libros"
        try:
            response = httpx.get(self.url)
            if response.status_code == 200:
                datos = response.json()
                return datos
            else:
                return response.status_code
        except httpx.RequestError as exc:
            print(f"Error de solicitud: {exc}")
            return None
        
class AutoresServiceApi():
    url = URLAPI
    def getAutoresAPI(self):
        # parametros = {"parametro1": "valor1", "parametro2": "valor2"}
        # headers = {"Authorization": "Bearer tu_token"}
        self.url += "/api/autores"
        try:
            response = httpx.get(self.url)
            if response.status_code == 200:
                datos = response.json()
                return datos
            else:
                return response.status_code
        except httpx.RequestError as exc:
            print(f"Error de solicitud: {exc}")
            return None
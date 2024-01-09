import psycopg

class connectionSql():
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=dbluis user=adminsemillero password=3113034506Lc host=semillerosudenar.postgres.database.azure.com port=5432")
        except psycopg.OperationalError as err :
            print(err)
            self.conn.close()

    def getConnection(self):
        return self.conn

    def __def__(self):
        self.conn.close()




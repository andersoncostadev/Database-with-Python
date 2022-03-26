from bd import connection_new
from mysql.connector.errors import ProgrammingError

try:
    with connection_new() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute('DROP TABLE emails')
        except ProgrammingError as error:
            print(f'Erro:{error.msg}')
except ProgrammingError as error:
    print(f'Erro CONECTION:{error.msg}')

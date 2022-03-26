from mysql.connector.errors import ProgrammingError
from bd import connection_new

sql = 'DELETE FROM contacts WHERE name = %s'
args = ('Lucas',)

with connection_new() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError() as error:
        print(f'Erro:{error.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) deletado(s)')

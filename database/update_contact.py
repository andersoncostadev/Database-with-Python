from mysql.connector.errors import ProgrammingError
from bd import connection_new

sql = 'UPDATE contacts SET name = %s WHERE id= %s'
args = ('Ana Lima', 2)

with connection_new() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError() as error:
        print(f'Erro:{error.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) alterado(s)')

from mysql.connector.errors import ProgrammingError
from bd import connection_new

sql = 'INSERT INTO contacts (name, phone) VALUES (%s, %s)'
args = ('Lucas', '98765-4321')

with connection_new() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        print('1 registro incluído, ID:', cursor.lastrowid)

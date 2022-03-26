from mysql.connector.errors import ProgrammingError
from bd import connection_new

sql = 'INSERT INTO groups (description) VALUES (%s)'
args = (
    ('Casa'),
    ('Trabalho'),
)

with connection_new() as connection:
    try:
        cursor = connection.cursor()
        cursor.executemany(sql, args)
        connection.commit()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        print('Foram incluídos {cursor.rowcount} registros!')

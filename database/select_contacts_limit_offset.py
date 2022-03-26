from mysql.connector.errors import ProgrammingError
from bd import connection_new

sql = 'SELECT * FROM contacts LIMIT %s OFFSET %s'
args = (3, 8)

with connection_new() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        contacts = cursor.fetchall()
    except ProgrammingError as error:
        print(f'Erro:{error.msg}')
    else:
        for contact in contacts:
            print(f'{contact[2]:2d} - {contact[0]:10s} Telefone:{contact[1]}')

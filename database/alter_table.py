from mysql.connector.errors import ProgrammingError
from bd import connection_new

sql = 'ALTER TABLE contacts ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'

with connection_new() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except ProgrammingError as error:
        print(f'Erro:{error.msg}')

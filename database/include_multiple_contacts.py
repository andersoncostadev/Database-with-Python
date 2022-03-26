from mysql.connector.errors import ProgrammingError
from bd import connection_new

sql = 'INSERT INTO contacts (name, phone) VALUES (%s, %s)'
args = (
    ('Ana', '97765-1321'),
    ('Bia', '99765-2321'),
    ('Luca', '96765-3321'),
    ('Lu', '90765-4321'),
    ('Gui', '91765-5321'),
    ('Beca', '92765-6321'),
    ('Pedro', '94765-7321'),
    ('João', '95765-8321'),
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

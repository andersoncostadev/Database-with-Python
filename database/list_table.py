from bd import connection_new

with connection_new() as connection:
    cursor = connection.cursor()
    cursor.execute('SHOW TABLES')

    for i, table in enumerate(cursor, start=1):
        print(f'Tabela {i}: {table[0]}')

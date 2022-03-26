from bd import connection_new

sql = 'SELECT name, id FROM contacts ORDER BY name DESC'

with connection_new() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)

    print('\n'.join(str(registro) for registro in cursor))

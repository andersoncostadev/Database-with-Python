from bd import connection_new

sql = 'SELECT * FROM contacts'

with connection_new() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)

    print(cursor.fetchone())

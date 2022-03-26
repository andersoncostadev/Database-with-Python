from bd import connection_new

sql = 'SELECT phone, name FROM contacts'

with connection_new() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)
    for contact in cursor.fetchall():
        print('\t'.join(str(field) for field in contact))

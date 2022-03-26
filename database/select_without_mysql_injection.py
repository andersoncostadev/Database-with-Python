from bd import connection_new

sql = "SELECT * FROM contacts WHERE name like %s "

with connection_new() as connection:
    name = input('Contato a localizar: ')
    args = (f'%{name}%', )

    cursor = connection.cursor()
    # Com o args de parametro não tera injection no bande dados
    cursor.execute(sql, args)

    for x in cursor:
        print(x)

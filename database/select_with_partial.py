from bd import connection_new

sql = "SELECT * FROM contacts WHERE name like 'Lu%' "

with connection_new() as connection:
    cusor = connection.cursor()
    cusor.execute(sql)

    for x in cusor:
        print(x)

from bd import connection_new

sql = "SELECT * FROM contacts WHERE phone = '98765-4321'"

with connection_new() as connection:
    cusor = connection.cursor()
    cusor.execute(sql)

    for x in cusor:
        print(x)

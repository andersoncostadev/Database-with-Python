from bd import connection_new

with connection_new() as connection:
    if connection.is_connected():
        print('Conectado!')

print('Fim!!')

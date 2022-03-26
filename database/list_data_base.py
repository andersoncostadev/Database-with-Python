from mysql.connector import connect

connection = connect(
    host='localhost',
    port=3306,
    user='root',
    password='22081988',
    auth_plugin='mysql_native_password'
)

cursor = connection.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print(f'Banco de Dados {i}: {database[0]}')

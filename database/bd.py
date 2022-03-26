from mysql.connector import connect
from contextlib import contextmanager


parameters = dict(
    host='localhost',
    port=3306,
    user='root',
    password='22081988',
    database='agenda',
    auth_plugin='mysql_native_password'
)


@contextmanager
def connection_new():
    connection = connect(**parameters)
    try:
        yield connection
    finally:
        if(connection and connection.is_connected()):
            connection.close()

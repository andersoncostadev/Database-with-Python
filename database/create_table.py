from bd import connection_new
from mysql.connector import ProgrammingError

table_contacts = """
  CREATE TABLE contacts(
    name VARCHAR(50), phone VARCHAR(40)
    )
"""

table_emails = """
  CREATE TABLE emails(
    id INT AUTO_INCREMENT PRIMARY KEY,
    owner VARCHAR(50)
  )
"""
try:
    with connection_new() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(table_contacts)
            cursor.execute(table_emails)
        except ProgrammingError as error:
            print(f'Erro:{error.msg}')
except ProgrammingError as error:
    print(f'Erro CONECTION:{error.msg}')

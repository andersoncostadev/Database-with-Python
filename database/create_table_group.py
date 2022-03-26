from bd import connection_new
from mysql.connector import ProgrammingError

table_groups = """
  CREATE TABLE grupo(
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(50)
  )
"""

change_contact_1 = """
  AlTER TABLE contacts ADD grupo_id INT
"""

change_contact_2 = """
  AlTER TABLE contacts ADD FOREIGN KEY (grupo_id)
  REFERENCES grupo(id)
"""
try:
    with connection_new() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(table_groups)
            cursor.execute(change_contact_1)
            cursor.execute(change_contact_2)
        except ProgrammingError as error:
            print(f'Erro:{error.msg}')
except ProgrammingError as error:
    print(f'Erro CONECTION:{error.msg}')

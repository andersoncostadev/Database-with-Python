from bd import connection_new
from mysql.connector.errors import ProgrammingError

sql = """
    SELECT
          grupo.description,
          contacts.name AS name
    FROM contacts
    INNER JOIN grupo ON contacts.group_id = group.id
    ORDER BY grupo, name
"""

with connection_new() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        contacts = cursor.fetchall()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        for contact in contacts:
            print(f'{contact["grupo"]}: {contact["name"]}')

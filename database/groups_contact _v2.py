from collections import defaultdict
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
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(sql)
            contacts = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        grouped = defaultdict(list)
        for contact in contacts:
            grouped[contact['grupo']].append(contact['name'])

        print(grouped)

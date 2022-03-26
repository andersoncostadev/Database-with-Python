from mysql.connector.errors import ProgrammingError
from bd import connection_new

select_group = 'SELECT id FROM grupo WHERE description = %s'
update_contact = 'UPDATE contacts SET group_id = %s WHERE name = %s'

contact_group = {
    'Ana Lima': 'Casa',
    'Bia': 'Trabalho',
    'Luca': 'Casa',
    'Lu': 'Trabalho',
    'Gui': 'Casa',
    'Beca': 'Casa',
    'Pedro': 'Trabalho',
    'João': 'Casa',
}

with connection_new() as connection:
    try:
        cursor = connection.cursor()
        for contact, grupo in contact_group.items():
            cursor.execute(select_group, (grupo,))
            group_id = cursor.fetchone()[0]
            cursor.execute(update_contact, (group_id, contact))
            connection.commit()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        print('Contatos associados !!')

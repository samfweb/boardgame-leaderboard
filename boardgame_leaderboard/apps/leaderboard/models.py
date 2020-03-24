from django.db import models
from django.db import connection

def get(table, *args):
    col_names = []
    for arg in args:
        col_names += arg
    if col_names:
        sql_select = ' '.join(col_names)
    else:
        sql_select = '*'
    
    with connection.cursor() as cursor:
        cursor.execute('SELECT %s FROM %s;', [sql_select, table])
        rows = dictfetchall(cursor)
        return rows
    
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]       

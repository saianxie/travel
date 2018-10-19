def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
        # for row in cursor.fetchone()
        # for row in cursor.fetchmany()
    ]
# from django.db import connection, connections
# from utils.util import dictfetchall
# cursor = connection.cursor()  # cursor = connections['default'].cursor()
# cursor.execute("""SELECT * from user_userinfo where leixing_id = %s limit 5""", [3])
# row = dictfetchall(cursor)
# print(row)

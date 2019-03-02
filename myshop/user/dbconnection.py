from django.db import connection

def executeQuery(query):
	cursor=connection.cursor()
	query_result=cursor.execute(query)
	columns = cursor.description
	return [dict(zip([col[0] for col in columns], row))
        for row in cursor.fetchall()]
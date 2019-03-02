from django.db import connection

def executeQuery(query):
	cursor=connection.cursor()
	query_result=cursor.execute(query)
	columns = cursor.description
	return [dict(zip([col[0] for col in columns], row))
        for row in cursor.fetchall()]

def execute(query):
    cur = connection.cursor()
    result = []
    try:
        cur.execute(query)
        if "INSERT" in query:
            return cur.lastrowid
        if 'UPDATE' in query:
            if cur.rowcount ==1 :
                return True
            else :
                return False
        columns = tuple( [d[0] for d in cur.description] )
        
        for row in cur:
            result.append(dict(zip(columns, row)))
    except Exception as e:
        print("Exception || {}".format(e))
    finally:
        cur.close()
    return result


import os
import pymysql

# Get username from GitPod
username = os.getenv('C9_USER')

# Connect to the database:
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query:
    with connection.cursor() as cursor:
        sql = 'select * from Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection to SQL after running the query, no matter if it was sucessful or not
    connection.close()

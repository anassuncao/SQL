import os
import datetime
import pymysql

# Get username from GitPod
username = os.getenv('C9_USER')

# Connect to the database:
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query: The following is the code up to the executemany function of the cursor
    """with connection.cursor() as cursor:
        rows = [('Bob', 21, '1990-02-06 23:04:56'),
                ('Jim', 56, '1955-05-09 13:12:45'),
                ('Fred', 100, '1911-09-12 01:01:01')]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()"""

    # The following code is from the update lesson onwards:
    """with connection.cursor() as cursor:
        cursor.execute('UPDATE Friends SET age = 22 where name = "Bob";')
        # An alternative to the UPDATE method:
        cursor.execute('UPDATE Friends SET age = %s where name = %s;',
                        (23, 'Bob'))
        connection.commit()

    # UPDATE many rows:
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (25, 'Fred')]
        cursor.executemany('UPDATE Friends SET age = %s where name = %s', rows)
        connection.commit()

    # DELETE one row from a table:
    with connection.cursor() as cursor:
        rows = cursor.execute('DELETE from Friends where name = "Bob";')
        connection.commit()

    #ALTERNATE DELETE using string interpelation (after adding Bob again to have more data):
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Bob')
        connection.commit()"""

    # DELETE MANY from a table:
    with connection.cursor() as cursor:
        rows = cursor.executemany('DELETE from Friends where name = %s;', ['Bob', 'Jim'])
        connection.commit()
finally:
    # Close the connection to SQL after running the query, no matter if it was sucessful or not
    connection.close()

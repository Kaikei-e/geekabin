import os

import pymysql.cursors

connection = pymysql.connect(host='172.16.230.30',
                             user=os.environ['MYSQL_USER'],
                             password=os.environ['PASSWORD'],
                             db=os.environ['geekabin'],
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `users`;"
        cursor.execute(sql)

        result = cursor.fetchone()
        print(result)
except Exception as e:
    print("Error: unable to fetch data: {}".format(e))

finally:
    # Close connection
    connection.close()
    print("Connection closed.")

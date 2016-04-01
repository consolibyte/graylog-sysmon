import sys
import pymysql.cursors

def monpymysql_run(config):
    connection = pymysql.connect(host=config['host'],
                                 user=config['username'],
                                 passwd=config['password'],
                                 db=config['database'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "SHOW GLOBAL STATUS"
            cursor.execute(sql, ())
            result = cursor.fetchone()

            print(result);

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    except:
        print(sys.exc_info()[0])

    finally:
        connection.close()
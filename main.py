import psycopg2

connection = psycopg2.connect(
            host="c-c9qhi5jpif1h5cqvlh32.rw.mdb.yandexcloud.net",
            port="6432",
            sslmode="verify-full",
            dbname="baron",
            user="itmo",
            password="baron-itmo",
            target_session_attrs="read-write",
        )
connection.autocommit = True

cursor = connection.cursor()
query = cursor.execute("insert into test.abc values('docker');")
connection.close()

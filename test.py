import psycopg2
conn=psycopg2.connect("dbname=project user=postgres")
cur=conn.cursor()
cur.execute("create table test (id serial primary key, num integer, data varchar);")
cur.execute("insert into test (num, data) values(%s, %s)",
        (100, "abc'def"))
cur.execute("select * from test;")
cur.fetchone()
conn.commit()
cur.close()
conn.close()

import psycopg2
conn = psycopg2.connect("dbname=mentorship user=dj")
cur=conn.cursor()
cur.execute("create table if not exists contestantinfo (contestantid serial primary key, contestid integer not null, graphic text not null, backgroundinfo text not null, name text not null);")
cur.execute("insert into contestantinfo (contestid, graphic, backgroundinfo, name) values (%s,%s,%s,%s)",
        (1, "null", "null", "name"))
cur.execute("create table if not exists contestinfo (id serial primary key, description text not null, name text not null);")
cur.execute("create table if not exists voterinfo (voter serial primary key, ip inet not null, target integer not null, timestamp timestamptz not null);")
conn.commit()
cur.execute("select * from contestantinfo;")
answer=cur.fetchone()
print(answer)
cur.close()
conn.close()

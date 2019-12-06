import psycopg2
def decorator(func):
    def wrapper(*args):
        conn=psycopg2.connect("dbname=mentorship user=dj")
        cur=conn.cursor()
        func(cur, *args)
        conn.commit()
        cur.close()
        conn.close()
    return wrapper
@decorator
def record_vote (cur, ip, target, timestamp):
    cur.execute(f"insert into voterinfo (ip, target, timestamp) values ('{ip}', '{target}', '{timestamp}')", (ip, target, timestamp))


@decorator
def add_contestant(cur, contest, graph, background, nam):
    cur.execute(f"insert into contestantinfo (contestid, graphic, backgroundinfo, name) values ({contest}, '{graph}', '{background}', '{nam}');")


@decorator
def reset_contestant_table(cur):
    cur.execute("drop table if exists contestantinfo;")
    cur.execute("create table contestantinfo (contestantid serial primary key, contestid integer not null, graphic text not null, backgroundinfo text not null, name text not null);")

@decorator
def reset_voter_table(cur):
    cur.execute("drop table if exists voterinfo;")
    cur.execute("create table voterinfo (voter serial primary key, ip inet not null, target integer not null, timestamp timestamptz not null);")

@decorator
def reset_contest_table(cur):
    cur.execute("drop table if exists contestinfo;")
    cur.execute("create table contestinfo (id serial primary key, description text not null, name text not null);")

@decorator
def add_contest(cur, description, name):
    cur.execute(f"insert into contestinfo (description, name) values ('{description}', '{name}')")
@decorator
def remove_contest(cur, name):
    cur.execute(f"delete from contestinfo where name='{name}'")

@decorator
def remove_vote(cur,voter, timestamptz):
    cur.execute(f"delete from voterinfo where voter='{voter}' and timestamp='{timestamptz}'")

@decorator
def remove_contestant(cur, name):
    cur.execute(f"delete from contestantinfo where name='{name}'")

@decorator
def create_table(cur, name, dinfo):
    b=(f"create table {name} ")
    a="(id serial primary key "
    for key in dinfo:
        a=a+(f", {key} {dinfo[key]}")
    cur.execute((b+a+");"))

@decorator
def destroy_table(cur, name):
    cur.execute(f"drop table if exists {name}")


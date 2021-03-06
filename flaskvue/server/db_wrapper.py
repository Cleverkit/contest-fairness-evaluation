import pdb
import psycopg2
def decorator(func):
    def wrapper(*args):
        conn=psycopg2.connect("dbname=mentorship user=dj")
        cur=conn.cursor()
        funvar=func(cur, *args)
        conn.commit()
        cur.close()
        conn.close()
        return funvar
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
    cur.execute("create table contestantinfo (id serial primary key, contestid integer not null, graphic text not null, backgroundinfo text not null, name text not null);")

@decorator
def reset_voter_table(cur):
    destroy_table("voterinfo")
    print("destroyed")
    create_table("voterinfo", {"ip":"inet not null", "target":"integer not null", "timestamp":"timestamptz not null"})
    print("created")

@decorator
def reset_contest_table(cur):
    print("begun")
    destroy_table("contestinfo")
    print("destroyed")
    create_table("contestinfo", {"description":"text not null", "name":"text not null"})
    print("created")

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
    repeat=0
    b=(f"create table if not exists {name} ")
    a="(id serial primary key"
    for key in dinfo:
        repeat+=1
        if ((repeat==len(dinfo)-1) or (len(dinfo)==1)):
            a=a+(f", {key} {dinfo[key]}")
            break
        a=a+(f", {key} {dinfo[key]},")
    cur.execute((b+a+");"))

@decorator
def destroy_table(cur, name):
    cur.execute(f"drop table if exists {name};")

@decorator
def get_table(cur, name):
    cur.execute(f"select * from {name};")
    notes=cur.fetchall()
    return notes

@decorator
def find_contestants(cur, contestid):
    cur.execute(f"select * from contestantinfo where contestid={contestid};")
    notes=cur.fetchall()
    return notes

@decorator
def find_votes(cur, target):
    cur.execute(f"select * from voterinfo where target={target};")
    notes=cur.fetchall()
    return notes


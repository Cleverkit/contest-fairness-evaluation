import unittest
import psycopg2
import db_wrapper
import pdb

class Testdb_wrapper(unittest.TestCase):
    def test_reset1(self):
        #pdb.set_trace()
        print("start reset contestant")
        #cur.execute("drop table if exists contestantinfo;")
        #cur.execute("create table contestantinfo (id serial primary key, contestid integer not null, graphic text not null, backgroundinfo text not null, name text not null);")
        db_wrapper.reset_contestant_table()
        cur.execute("select case when exists (select * from contestantinfo limit 1) then 1 else 0 end;")
        results=cur.fetchone()
        print(results, (0,))
        self.assertEqual(results, (0,))

    def test_reset2(self):
        print("start reset contest")
        #cur.execute("drop table if exists contestinfo;")
        #cur.execute("create table contestinfo (id serial primary key, description text not null, name text not null);")
        db_wrapper.reset_contest_table()
        cur.execute("select case when exists (select * from contestinfo limit 1) then 1 else 0 end;")
        results=cur.fetchone()
        print(results, (0,))
        self.assertEqual(results, (0,))

    def test_reset3(self):
        print("start reset voter")
        #cur.execute("drop table if exists voterinfo;")
        #cur.execute("create table voterinfo (id serial primary key, ip inet not null, target integer not null, timestamp timestamptz not null);")
        db_wrapper.reset_voter_table()
        cur.execute("select case when exists (select * from voterinfo limit 1) then 1 else 0 end;")
        results=cur.fetchone()
        print(results, (0,))
        self.assertEqual(results, (0,))

    def test_destroy(self):
        print("start destroy")
        db_wrapper.destroy_table("test")
        cur.execute("select exists(select 1 from information_schema.tables where table_schema = 'public' and table_name = 'test');")
        results=cur.fetchone()
        print(results, (False,))
        self.assertEqual(results, (False,))

    def test_create(self):
        print("start create")
        db_wrapper.destroy_table("test")
        db_wrapper.create_table("test", {"next":"int", "wayforward":"text"})
        cur.execute("select exists(select 1 from information_schema.tables where table_schema = 'public' and table_name = 'test');")
        results=cur.fetchone()
        print(results, (True,))
        self.assertEqual(results, (True,))

    def test_add_contestant(self):
        print("start add contestant") 
        db_wrapper.add_contestant(1, "thing", "link1", "tester")
        cur.execute("select * from contestantinfo;")
        results=cur.fetchone()
        print(results, (1, 1, 'thing', 'link1', 'tester'))
        self.assertEqual(results, (1, 1, 'thing', 'link1', 'tester'))

    def test_add_contest(self):
        print("start add contest")
        db_wrapper.reset_contest_table()
        cur.execute("select case when exists (select * from contestinfo limit 1) then 1 else 0 end;")
        final=cur.fetchone()
        print("the results of the reset test is "+str(final))
        db_wrapper.add_contest('chess system', 'Elo')
        cur.execute("select * from contestinfo;")
        results=cur.fetchone()
        print(results, (1, "chess system", "Elo"))
        self.assertEqual(results, (1, "chess system", "Elo"))

    def test_add_voter(self):
        print("start add voter")
        db_wrapper.record_vote('198.10/8', 2, '2016-06-22 19:10:25-07')
        cur.execute("select ip from voterinfo;")
        results=cur.fetchone()
        print(results, ("198.10.0.0/8", ))
        self.assertEqual(results, ('198.10.0.0/8', ))



conn=psycopg2.connect("dbname=mentorship user=dj")
cur=conn.cursor()
conn.autocommit=True
if __name__ == '__main__':
    unittest.main()
    cur.close()
    conn.close()


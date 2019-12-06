import unittest
import psycopg2
import db_wrapper


class Testdb_wrapper(unittest.TestCase):
    def test_reset1(self):
        db_wrapper.reset_contestant_table()
        cur.execute("select case when exists (select * from contestantinfo limit 1) then 1 else 0 end;")
        self.assertEqual(cur.fetchone(), (0,))

    def test_reset2(self):
        db_wrapper.reset_contest_table()
        cur.execute("select case when exists (select * from contestinfo limit 1) then 1 else 0 end;")
        self.assertEqual(cur.fetchone(), (0,))

    def test_reset3(self):
        db_wrapper.reset_voter_table()
        cur.execute("select case when exists (select * from voterinfo limit 1) then 1 else 0 end;")
        self.assertEqual(cur.fetchone(), (0,))

    def test_destroy(self):
        db_wrapper.destroy_table("test")
        cur.execute("select exists(select 1 from information_schema.tables where table_schema = 'public' and table_name = 'test');")
        self.assertEqual(cur.fetchone(), (False,))

    def test_create(self):
        db_wrapper.create_table("test", {"next":"int", "wayforward":"text"})
        cur.execute("select exists(select 1 from information_schema.tables where table_schema = 'public' and table_name = 'test');")
        self.assertEqual(cur.fetchone(), (True,))
    
   # def test_add_contestant(self):
    #    db_wrapper.add_contestant(1, "thing", "link1", "tester")
     #   db_wrapper.add_contestant(2, "thing2", "link2", "doomed")
      #  cur.execute("select * from contestantinfo")
       # self.assertEqual(cur.fetchone(), "((1, 1, 'thing', 'link1', 'tester'), (2, 2, 'thing2', 'link2', 'doomed'))")

#    def test_add_contest(self):
 #       db_wrapper.add_contest('chess system', 'Elo')
  #      db_wrapper.add_contest('penny, print', 'pound')
   #     self.assertEqual(cur.execute("select * from contestinfo"), "((1, 'chess system', 'Elo'), (2, 'penny, print', 'pound'))")

    def test_add_voter(self):
        db_wrapper.record_vote('198.10/8', 2, '2016-06-22 19:10:25-07')
        db_wrapper.record_vote('198.9/8', 1, '2016-06-23 19:10:25-07')
        conn.commit()
        cur.execute("select timestamp from voterinfo;")
        self.assertEqual(cur.fetchone(), "((1, '198.10.0.0/8', 2, datetime.datetime(2016, 6, 22, 22, 10, 25, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=-240, name=None))), (2, '198.9.0.0/8', 1, datetime.datetime(2016, 6, 23, 22, 10, 25, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=-240, name=None))")

conn=psycopg2.connect("dbname=mentorship user=dj")
cur=conn.cursor()
if __name__ == '__main__':
    unittest.main()
    cur.close()
    conn.close()

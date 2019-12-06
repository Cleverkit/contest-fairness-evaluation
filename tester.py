import psycopg2
import db_wrapper
conn=psycopg2.connect("dbname=mentorship user=dj")
cur=conn.cursor()
db_wrapper.reset_contestant_table()
db_wrapper.reset_contest_table()
db_wrapper.reset_voter_table()
db_wrapper.destroy_table("test")
db_wrapper.create_table("test", {"next":"int","wayforward":"text"})
db_wrapper.add_contestant(1, "thing", "link1", "tester")
db_wrapper.add_contestant(2, "thing2", "link2", "doomed")
db_wrapper.record_vote('198.9/8', 1, '2016-06-23 19:10:25-07')
db_wrapper.add_contest("chess system", "Elo")
db_wrapper.add_contest("penny, print", "pound")
conn.commit()
cur.execute("select * from test")
print(cur.fetchone())
cur.execute("select * from contestinfo;")
print(cur.fetchone())
cur.execute("select contestantid from contestantinfo;")
print(cur.fetchone())
cur.execute("select * from voterinfo;")
print(cur.fetchone())
cur.close()
conn.close()






import json
import db_wrapper
import pdb
def processjson(myjson, action):
    myjson=json.loads(myjson)
    if action=="record_vote":
        db_wrapper.record_vote(myjson["ip"], myjson["target"], myjson["timestamp"])
        return ("Vote admitted")
    elif action=="add_contestant":
        db_wrapper.add_contestant(myjson["contest"], myjson["graph"],myjson["background"], myjson["name"])
        return ("Add Request acknowledged")
    elif action=="reset_contestant_table":
        db_wrapper.reset_contestant_table()
        return ("Reset accepted")
    elif action=="add_contest":
        db_wrapper.add_contest(myjson["description"], myjson["name"])
        return ("Add Request acknowledged")
    elif action=="remove_contest":
        db_wrapper.remove_contest(myjson["name"])
        return ("Removal accepted")
    elif action=="remove_vote":
        db_wrapper.remove_vote(myjson["voter"], myjson["timestamptz"])
        return ("Removal accepted")
    elif action=="remove_contestant":
        db_wrapper.remove_contestant(myjson["name"])
        return("Removal accepted")
    elif action=="get_table":
        return db_wrapper.get_table(myjson["name"])
    elif action=="find_contestants":
        return db_wrapper.find_contestants(myjson["contestid"])
    elif action=="find_votes":
        return db_wrapper.find_votes(myjson["target"])
    elif action=="create_table":
        del myjson["command"]
        name=myjson["name"]
        del myjson["name"]
        db_wrapper.create_table(name, myjson)
        return db_wrapper.get_table(name)
    else:
        return ("No action found")


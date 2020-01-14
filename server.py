import json
import db_wrapper
def processjson(myjson):
    if action=="record_vote":
        db_wrapper.record_vote( [0], [1], [2])
        return ("Vote admitted")
    elif action=="add_contestant":
        db_wrapper.add_contestant(*args)
        return ("Add Request acknowledged")
    elif action=="reset_contestant_table":
        db_wrapper.reset_contestant_table()
        return ("Reset accepted")
    elif action=="add_contest"):
        db_wrapper.add_contest(*args)
        return ("Add Request acknowledged")
    elif action=="remove_contest":
        db_wrapper.remove_contest(*args)
        return ("Removal accepted")
    elif action=="remove_vote":
        db_wrapper.remove_vote(*args)
        return ("Removal accepted")
    elif action=="remove_contestant":
        db_wrapper.remove_contestant(*args)
        return("Removal accepted")
    else:
        return ("No action found")
processjson(

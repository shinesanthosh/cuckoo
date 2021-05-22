from replit import db


def getid():
    last_id = db["last_id"]
    print(f"Last id is: {last_id}")
    return last_id


def setid(id):
    db["last_id"] = id
    getid()

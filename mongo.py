import pymongo
import os

if os.path.exists("env.py"):
    import env


MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# INSERT
"""new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '23/05/1952', 'hair_colour': 'red', 'occupation': 'writer', 'nationality': 'english'}, {'first': 'roy', 'last': 'keane', 'dob': '23/05/1972', 'hair_colour': 'brown', 'occupation': 'football player', 'nationality': 'irish'}]

coll.insert_many(new_docs)"""

# DELETE
# coll.delete_one({'first': 'douglas'})

# UPDATE
# coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

coll.update_many({'nationality': 'irish'}, {'$set': {'hair_colour': 'red'}})

documents = coll.find()

for doc in documents:
    print(doc)

import pymongo
import datetime

cluster = "mongodb+srv://tylermchambers92:Pyamp123@cluster.m2o0e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"

client = pymongo.MongoClient(cluster)

# print(client.list_database_names())

db = client.TestDB

# print(db.list_collection_names())

todo = {"name": "Tyler",
        "text": "My first todo!",
        "status": "open",
        "tags": ["python", "coding"],
        "data": datetime.datetime.now()}

todos = db.ToDo

# result = todos.insert_one(todo)

todo2 = [
            {
                "name": "Luke",
                "text": "My second todo!",
                "status": "open",
                "tags": ["python", "coding"],
                "data": datetime.datetime.now()},
            {
                "name": "Haley",
                "text": "My third todo!",
                "status": "open",
                "tags": ["c++", "coding"],
                "data": datetime.datetime.now()}]

# add multiple entries
# result2 = todos.insert_many(todo2)

# find an entry
# result = todos.find_one({"name": "Luke"})

# result = todos.find_one({"tags": "c++"})

# find by object id
# from bson.objectid import ObjectId
# result = todos.find_one({"_id": ObjectId("6724cbe48e92f3a15cff0ea8")})

# find multiple returns a list
# result = todos.find({'name': 'Tyler'})

# prints the number of entries containing the below
print(todos.count_documents({"tags": "python"}))

# remove an entry
# from bson.objectid import ObjectId
# result = todos.delete_one({"_id": ObjectId("6724cbe48e92f3a15cff0ea8")})

# delete many
# result = todos.delete_many({"name": "Tyler"})

# delete all
# result = todos.delete_many({})

# update one
# result = todos.update_one({"name": "Luke"}, {"$set": {"name": "Lukey"}})

# remove key value pair
# you can also use $set to add a new key/value pair
# result = todos.update_one({"name": "Luke"}, {"$unset": {"name": "Lukey"}})

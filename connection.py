from pymongo import MongoClient

# mongodb://user:password@host:port
uri = 'mongodb://root:example@localhost:27017/'
client = MongoClient(uri)


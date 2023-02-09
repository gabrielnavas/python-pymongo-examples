from connection import client

database_live = client['live']
pessoas_collection = database_live['pessoas']

pessoas_collection.find_one_and_delete({ "name": "jose" })

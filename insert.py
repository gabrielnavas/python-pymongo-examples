from pprint import pprint

from connection import client

database_live = client['live']
pessoas_collection = database_live['pessoas']

# insert
pessoas_collection.insert_one({ "name":'jucas', "idade": 15 })
pessoas_collection.insert_one({ "name":'jose', "idade": 16 })
pessoas_collection.insert_one({ "name":'lucas', "idade": 17 })
pessoas_collection.insert_one({ "name":'juliana', "idade": 18 })
pessoas_collection.insert_one({ "name": 'marcio', "idade": 19})

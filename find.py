from pprint import pprint

from connection import client

database_live = client['live']
pessoas_collection = database_live['pessoas']

# operadores
equals = '$eq'
not_equals = '$ne'
great_than = '$gt'
great_than_equal = '$gte'
less_than = '$lt'
less_than_equal = '$lte'
op_in = '$in'
op_not_in = '$nin'
exists = '#exists'

# query
pprint(
    list(
        pessoas_collection.find( 
            { 
                "$and": [ 
                    { "idade": { "$gt": 15 } }, 
                    { "idade": { "$lt": 17 } }, 
                    { "idade": { "$exists": True } } 
                ]
            } 
        )
    )
)
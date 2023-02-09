from connection import client

database_live = client['live']
pessoas_collection = database_live['pessoas']

# usar o $set ele apenas atualiza o documento encontrado
# caso não usar o $set ele atualiza o documento inteiro

pessoas_collection.find_one_and_update(
    { "name": "jucas"},  
    { "$set": { "name": "josefino@@@@@@@@@" }}
)
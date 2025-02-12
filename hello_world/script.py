from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@localhost:27017/',authSource='admin')

db = client['mydatabase']

collection = db['mycollection']

document = {'name': "Alisa", 'age':20, 'city': "SPb"}
insert_result = collection.insert_one(document)

print(f'Вставленный ID: {insert_result.inserted_id}')

query = {'name': 'Alisa'}
found_document = collection.find_one(query)
print(f'Найденный документ: {found_document}')

update_query = {'name': "Alisa"}
new_values = {'$set': {'age':19}}
collection.update_one(update_query, new_values)
print("Документ обновлен")


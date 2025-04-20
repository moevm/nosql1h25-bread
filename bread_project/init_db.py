# user_profile/mongo_init.py

import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

# Загружаем .env
load_dotenv()

def init_collections():
    client = MongoClient(
        host=os.getenv('MONGO_HOST', 'localhost'),
        port=int(os.getenv('MONGO_PORT', 27017)),
        username=os.getenv('MONGO_USERNAME'),
        password=os.getenv('MONGO_PASSWORD'),
        authSource='admin'
    )
    db = client[os.getenv('MONGO_DB', 'mydb')]

    # JSON‑Schema для коллекций
    schemas = {
        'User': {
            'bsonType': 'object',
            'required': [
                'UserID','Name','Surname','Nickname',
                'Create_Date','Last_Redact_Date',
                'email','CommentIDs','hash_Password'
            ],
            'properties': {
                'UserID':           {'bsonType': 'string'},
                'Name':             {'bsonType': 'string'},
                'Surname':          {'bsonType': 'string'},
                'Nickname':         {'bsonType': 'string'},
                'Create_Date':      {'bsonType': 'date'},
                'Last_Redact_Date': {'bsonType': 'date'},
                'email':            {'bsonType': 'string'},
                'CommentIDs': {
                    'bsonType': 'array',
                    'items': {'bsonType': 'int'}
                },
                'hash_Password':    {'bsonType': 'string'},
            }
        },
        'Recipe': {
            'bsonType': 'object',
            'required': [
                'RecipeID','Title','Composition',
                'Date','Recipe','Rate','CommentIDs'
            ],
            'properties': {
                'RecipeID':   {'bsonType': 'string'},
                'Title':      {'bsonType': 'string'},
                'Composition':{'bsonType': 'string'},
                'Date':       {'bsonType': 'date'},
                'Recipe':     {'bsonType': 'string'},
                'Rate':       {'bsonType': 'int'},
                'CommentIDs': {
                    'bsonType': 'array',
                    'items': {'bsonType': 'int'}
                },
            }
        },
        'Comment': {
            'bsonType': 'object',
            'required': [
                'CommentID','Username','Text',
                'Rating','Date','RecipeID','Title'
            ],
            'properties': {
                'CommentID': {'bsonType': 'string'},
                'Username':  {'bsonType': 'string'},
                'Text':      {'bsonType': 'string'},
                'Rating':    {'bsonType': 'int'},
                'Date':      {'bsonType': 'date'},
                'RecipeID':  {'bsonType': 'int'},
                'Title':     {'bsonType': 'string'},
            }
        },
    }

    # Индексы: (поле, unique)
    indexes = {
        'User':    [('UserID', True), ('email', True)],
        'Recipe':  [('RecipeID', True)],
        'Comment': [('CommentID', True), ('RecipeID', False)],
    }

    for name, schema in schemas.items():
        if name not in db.list_collection_names():
            try:
                db.create_collection(
                    name,
                    validator={'$jsonSchema': schema},
                    validationLevel='strict'
                )
                print(f'→ Created collection `{name}`')
            except CollectionInvalid:
                print(f'! Failed to create `{name}`')
        else:
            print(f'✔ Collection `{name}` already exists')

        for field, unique in indexes[name]:
            db[name].create_index(field, unique=unique)
            print(f'   ↳ Index on `{field}` (unique={unique})')

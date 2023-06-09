from db.mongodb import MongoDB

if __name__ == '__main__':
    print('teste123')

    url = 'mongodb://localhost:27017/'
    db_name = 'my_database'
    mongo = MongoDB(url, db_name)

    print(mongo)

    # document = {"name": "Mary", "age": 29}
    # mongo.insert("my_collection", document)

    print(list(mongo.find('my_collection')))
    print(list(mongo.find('my_collection', {'name': 'John'})))
 
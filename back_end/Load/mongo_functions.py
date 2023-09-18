import pymongo #needed?

def create_db(my_client, db_name, collection_name):
    my_client[db_name][collection_name]

def add_data_db_many(my_client, db_name, collection_name, data):
    my_client[db_name][collection_name].insert_many(data)
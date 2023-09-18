from Load.mongo_functions import create_db, add_data_db_many
import pymongo #needed?
#other function CrUD see previous py-file, this is main function

def mongo(my_client, db_name, collection_name, data): #todo: add my_client in calling function in main.py
    if db_name in my_client.list_database_names():
        my_client.drop_database(db_name)
    create_db(my_client, db_name, collection_name)
    add_data_db_many(db_name, collection_name, data)

#strucutre mongo type to say the metric in dictionary, see existing structure. Strategy as folder as well??
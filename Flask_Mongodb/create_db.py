import pymongo
from url_connection import url
from datetime import datetime


def pull_interfaces_info(collection, switch_name, ifz_name, description, state):
    document = {
        "Switch_name" : switch_name,
        "Interface_Name" : ifz_name,
        "Description" : description,
        "State" : state
    }
    document_id = collection.insert_one(document).inserted_id
    print(f'Created a document with id: {document_id}')




with pymongo.MongoClient(url) as client:
    db=client.Device_Configuration
    collection = db.Interfaces

    pull_interfaces_info(collection, "bru-dna-1", "g1/0", "Connected to the switch2 gi1/2", "Up")
    pull_interfaces_info(collection, "bru-dna-1", "fc1/1/0", "Connected to the storage port 1", "Up")
    pull_interfaces_info(collection, "mastodon", "GigabitEthernet1/0/3", "Connected to printer CX2", "Up")
    pull_interfaces_info(collection, "mastodon", "GigabitEthernet1/0/5", "Connected to printer CX4", "Down")
    pull_interfaces_info(collection, "mastodon", "GigabitEthernet1/4/3", "Connected to server SERV1", "Up")


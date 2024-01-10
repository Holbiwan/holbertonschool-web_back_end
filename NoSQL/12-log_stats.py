#!/usr/bin/python3
"""log stats"""
from pymongo import MongoClient


def count_all(mongo_collection):
    """counts all documents in a collection

    :param mongo_collection: pymongo collection object

    """
    return mongo_collection.count_documents({})


def count_method(mongo_collection, method):
    """counts all documents in a collection with a particular method

    :param mongo_collection: pymongo collection object
    :param method: method to be searched

    """
    return mongo_collection.count_documents({"method": method})


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = client.logs
    nginx = logs_db.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("{} logs".format(count_all(nginx)))
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method, count_method(nginx, method)))
    print("{} status check".format(
        count_method(nginx, {"method": "GET", "path": "/status"})))

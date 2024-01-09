#!/usr/bin/python3
"""log_stats"""

from pymongo import MongoClient


def count_all(mongo_collection):
    """counts all documents in a collection"""
    return mongo_collection.count()


def count_method(mongo_collection, method):
    """counts all documents in a collection with a particular method"""
    return mongo_collection.count({"method": method})


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print("{} logs".format(count_all(nginx)))
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method, count_method(nginx, method)))

    print("{} status check".format(
        nginx.count({"method": "GET", "path": "/status"})))

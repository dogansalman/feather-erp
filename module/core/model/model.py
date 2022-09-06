import string
import json
from sql import Sql

class Model(Sql):

    def __init__(self) -> None:
        pass
    

    # Todo get field name and type from postgress for cast json object
    # use redis cache
    # https://levelup.gitconnected.com/implement-api-caching-with-redis-flask-and-docker-step-by-step-9139636cef24
    def getMeta():
        Sql.run("....")
        pass
        

    # Generate create query from json object in request with cast metaData
    def create(json: json, path: string):
        Sql.run("....")
        pass

    # Generate read query from 
    def read(id: int, path: string):
        Sql.run("....")
        pass

    # update delete query
    def update(json: json, path: string):
        Sql.run("....")
        pass

    # Generate delete query
    def delete(id: int, path: string):
        Sql.run("....")
        pass

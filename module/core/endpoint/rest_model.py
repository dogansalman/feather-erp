from flask_restful import reqparse, abort, Api, Resource
from model.model import Model

# Path ile ilgili class ı import edip. aşağıdaki methodları çalıştırabiliriz.
# before_save
# after_save
# on_read
# on_delete

# shows a single model and delete or update item.
class RestModel(Resource):
    
    # Todo
    def __init__(self) -> None:
        pass
    
    def get(self, path, id):
        return {'path': 'path is ' + path + " id --> " + id}, 200

    def delete(self, path, id):
        return 'delete', 204

    def put(self, path, id):
        return "put", 201


# shows a list of all model, and lets you POST to add new model 
class RestModelList(Resource):
    def get(self, path):
        return [], 200

    def post(self, path):
        content = reqparse.request.json
        return content, 201

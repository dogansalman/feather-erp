from flask_restful import reqparse, abort, Api, Resource
import os

class AbstractRest(Resource):
    
    def __init__(self) -> None:
        pass
    
    def get(self, path, id):
        return {'path': "id --> in abstractRest" + id}, 200

    def delete(self, path, id):
        return 'delete', 204

    def put(self, path, id):
        return "put", 201
    



# shows a list of all model, and lets you POST to add new model 
class AbstractRestList(Resource):
    def get(self, path):
        return [], 200

    def post(self, path):
        # content = reqparse.request.json
        content = os.path.abspath(os.curdir)/"model/"
        return content, 201

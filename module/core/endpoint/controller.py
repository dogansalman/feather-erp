
from flask_restful import Api
from flask import Flask
from module.core.endpoint.rest_model import RestModel, RestModelList

class Controller():

    def __init__(self, app: Flask) -> None:

      ## Set the Api resource routing here
      api = Api(app)
      api.add_resource(RestModel, '/<path>/<id>')
      api.add_resource(RestModelList, '/<path>')

  

        

   
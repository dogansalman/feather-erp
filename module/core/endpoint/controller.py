
from flask_restful import Api
from flask import Flask
from module.core.endpoint.rest_model import RestModel, RestModelList
from  module.core.endpoint.abstract_rest import AbstractRest, AbstractRestList
class Controller():

    def __init__(self, app: Flask) -> None:
      api = Api(app)


      ## Set the Api resource routing here
      api.add_resource(AbstractRest, '/<path>/<id>')
      api.add_resource(AbstractRestList, '/<path>')


      ## Set the model resource routing here
      api.add_resource(RestModel, '/model/<id>')
      api.add_resource(RestModelList, '/model')

  

        

   
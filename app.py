from flask import Flask, request_started
from module.core.security.interceptor import requestFilter
from module.core.endpoint.controller import Controller

app = Flask(__name__)


# Init app
class App(Controller):        
    if __name__ == '__main__':
        controller = Controller(app)
        request_started.connect(requestFilter, app)
        app.run(port = 9090)





from flask import Flask, request_started
from interceptor import requestFilter


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'



if __name__ == '__main__':
    request_started.connect(requestFilter, app)
    app.run(port = 9090)



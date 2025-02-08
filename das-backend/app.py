from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

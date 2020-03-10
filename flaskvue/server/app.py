from flask import Flask, jsonify, request
from flask_cors import CORS
import server
import json

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': "*"}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/api', methods=['GET', 'POST'])
def api():
    data=request.args
    data=dict(data)
    action=data['command']
    del data['command']
    print (data)
    return(str(server.processjson(json.dumps(data), action)))
    


if __name__ == '__main__':
    app.run()

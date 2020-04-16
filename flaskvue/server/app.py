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
    #print(data)
    #print(data.copy())
    
    data=data.to_dict(flat=True)
    action=data.get('command')
    data.pop('command')
    lister=server.processjson(json.dumps(data), action) 
    fixer=(lister[0][0])
    final={"data":fixer}
    print (json.dumps(final))
    return json.dumps(final)
if __name__ == '__main__':
    app.run()

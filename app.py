from flask import Flask
from flask import request
import json
from flask import jsonify
from Send_osc import Send_osc

app = Flask(__name__)

@app.route('/toTree', methods=['POST'])
def postPronpt():
    data = request.get_data().decode('utf-8')
    data = json.loads(data)
    client = Send_osc(data['prompt'])
    client.send()
    return 'OK'

from flask import Flask,Response, render_template, request, jsonify, make_response, send_from_directory, redirect, url_for
import json
import pymongo


app = Flask(__name__)


mongo = pymongo.MongoClient("mongodb://admin:123456@mongo:27017/")
db = mongo['admin']
value_col= db['pulse_service']


@app.route('/pulse_list', methods=['GET'])
@app.route('/', methods=['GET'])
def data_list():
    pulse_value = value_col.find_one({},{ "_id": 0})    
    return Response(json.dumps(pulse_value,indent = 4),mimetype='application/json')    


if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)

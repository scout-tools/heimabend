import uuid
import json

from pymongo import MongoClient
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from bson.json_util import dumps

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

client = MongoClient('localhost:27017')
db = client.geo

@app.route("/ringMember", methods = ['POST', 'PUT'])
def add_contact():
    if request.method == 'POST':
        data = json.loads(request.data)
        stamm = data['stamm']
        city = data['city']
        members = data['members']
        latitude = data['latitude']
        longitude = data['longitude']
        if stamm and city and members and latitude and longitude:
            db.ringMembers.insert_one({
                'id': uuid.uuid4().hex,
                "stamm" : stamm,
                "city" : city,
                "members" : members,
                "latitude" : latitude,
                "longitude" : longitude
            })
        return dumps({'message' : 'SUCCESS'})
    if request.method == 'PUT':
        data = json.loads(request.data)
        id_data = data['id']
        stamm = data['stamm']
        city = data['city']
        members = data['members']
        latitude = data['latitude']
        longitude = data['longitude']
        if id_data and stamm and city and members and latitude and longitude:
            myquery = { "id": id_data }
            newData = {
                "$set": {
                    "stamm" : stamm,
                    "city" : city,
                    "members" : members,
                    "latitude" : latitude,
                    "longitude" : longitude
                }
            }
            db.ringMembers.update_one(myquery, newData)
        return dumps({'message' : 'SUCCESS'})

@app.route("/ringMember/<ringMember_id>", methods=["DELETE"])
def single_member(ringMember_id):
    response_object = {'status': 'success'}
    if request.method == 'DELETE':
        myquery = { "id": ringMember_id}
        db.ringMembers.delete_one(myquery)
    return jsonify(response_object)

@app.route("/ringMembers", methods = ['GET'])
def getRingMembers():
    ringMembers = db.ringMembers.find()
    return dumps(ringMembers)


if __name__ == '__main__':
    app.run()
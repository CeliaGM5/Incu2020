from flask import Flask, json, jsonify
from flask import render_template
from bson import json_util
import pymongo
from url_connection import url



app = Flask(__name__)

json.dumps = json_util.dumps

@app.route("/<switch_name>/interfaces.html", methods=["GET"])
def get_switch_info(switch_name):
    with pymongo.MongoClient(url) as client:
        db = client.Device_Configuration
        collection = db.Interfaces

        # Getting data
        cursor = collection.find({'Switch_name': switch_name})
    return render_template('interfaces.html', switch = switch_name, data = cursor)


@app.route("/<switch_name>/interfaces.json", methods=["GET"])
def get_switch_info_json(switch_name):
    dict_switch = {}
    dict_sw = {}
    with pymongo.MongoClient(url) as client:
        db = client.Device_Configuration
        collection = db.Interfaces

        # Getting data
        cursor = collection.find({'Switch_name': switch_name})
        i=1
        for result in cursor:
            for key, value in result.items():
                dict_sw[key] = value
            dict_switch[i] = dict_sw
            i+=1

    return jsonify(dict_switch)


@app.route("/<switch_name>/<interface>/details.html", methods=["GET"])
def get_ifz_info(switch_name, interface):
    with pymongo.MongoClient(url) as client:
        db = client.Device_Configuration
        collection = db.Interfaces
        interface = interface.replace("-", "/")
        # Getting data
        cursor = collection.find({'Switch_name': switch_name , 'Interface_Name': interface})
    return render_template('details.html', switch = switch_name, interface = interface, data = cursor)


@app.route("/<switch_name>/<interface>/details.json", methods=["GET"])
def get_ifz_info_json(switch_name, interface):
    dict_ifz = {}
    with pymongo.MongoClient(url) as client:
        db = client.Device_Configuration
        collection = db.Interfaces
        interface = interface.replace("-", "/")
        # Getting data
        cursor = collection.find({'Switch_name': switch_name , 'Interface_Name': interface})
        for result in cursor:
            for key, value in result.items():
                dict_ifz[key] = value
    return jsonify(dict_ifz)


if __name__ == '__main__':
    app.run()

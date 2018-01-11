import config
import requests
import json
from flask import Flask, jsonify

# url = "https://app.mrpeasy.com/rest/v1/manufacturing-orders/"
BASE_URL = "https://app.mrpeasy.com/rest/v1/"

BASE_HEADERS = {
    "api_key": config.api_key,
    "access_key": config.access_key}

app = Flask(__name__)

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def catch_all(path):
    url_id = BASE_URL + "%s" % path
    return jsonify(MRPeasy_response(url_id))

def MRPeasy_response(url):
    myResponse = requests.get(url, headers=BASE_HEADERS)

    # For successful API call, response code will be 200 (OK)
    if myResponse.ok:
    # Loading the response data into a dict variable
        jData = json.loads(myResponse.content)

        # print("The response contains {0} properties".format(len(jData)))
        # print("\n")
        for key in jData:
            print(key)
            print("\n")
        return jData
    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

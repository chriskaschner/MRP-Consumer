import config
import requests
import json
from flask import Flask, jsonify

# url = "https://app.mrpeasy.com/rest/v1/manufacturing-orders/"
base_url = "https://app.mrpeasy.com/rest/v1/"

headers = {
    "api_key": config.api_key,
    "access_key": config.access_key}

app = Flask(__name__)

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def catch_all(path):
    url_id = base_url + "%s" % path
    return jsonify(MRPeasy_response(url_id))

# @app.route('/', defaults={'path': ''})
# def root():
#     url = "https://app.mrpeasy.com/rest/v1/manufacturing-orders/"
#     response_list = str(MRPeasy_response(url))
#     return response_list

# def api_response(path):
#     url_id = path 
#     # api response from a given url
#     return str(MRPeasy_response(url_id))

def MRPeasy_response(url):
    myResponse = requests.get(url, headers=headers)

    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):
    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
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
    
# enter desired url of mrp easy
# format and attach authentication
# send request to mrp easy api
# format response
# send response
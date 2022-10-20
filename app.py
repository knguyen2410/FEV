from flask import Flask, render_template,request
import requests
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# from ibm_platform_services.iam_identity_v1 import *
from ibm_platform_services import IamIdentityV1

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/form")
def form():
    return render_template("form.html")

@app.route('/result',methods =["GET", "POST"])

def result():
    output = request.form.to_dict()
    if (output["state"] != "NJ"):
        return render_template("form.html", message = "This location is not currently supporting.")
    else:
        #access token
        headers_token = {
            'accept': 'application/json',
        }

        data_token = {
            'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
            'apikey': 'zC1_2chUco43B7fdCEw1agYntA62d3JE-dEdzW5RNo0Q',
        }

        response_token = requests.post('https://iam.cloud.ibm.com/identity/token', headers=headers_token, data=data_token)
        json_object = json.loads(response_token.text)

        #fetch api
        headers = {
        'accept': 'application/json',
        'authorization': 'Bearer ' + json_object["access_token"],
        }
        params = {
            'blocking': 'true',
        }
        data = {
            "race": output["Race"], #get from front end
            "county": output["county"] #get from front end
        }

        response = requests.post('https://us-east.functions.cloud.ibm.com/api/v1/namespaces/26095e4b-8f64-4b8f-b1b6-59b7376c4898/actions/vaccine-algo-api-1', params=params, json = data, headers=headers)
        response = dict(json.loads(response.text))
        return render_template("form.html", response=response["response"]["result"])

@app.route("/info")

def info():
    return render_template("info.html")


if __name__=="__main__":
    app.run(debug=True, port=5001)



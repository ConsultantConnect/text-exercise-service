import os
import requests

from flask import Flask, request, jsonify
from flask_cors import cross_origin

app = Flask(__name__)
app.config["DEBUG"] = True

ACCOUNT = os.environ.get('TWILIO_ACCOUNT_SID', None)
TOKEN = os.environ.get('TWILIO_ACCOUNT_TOKEN', None)
FROM = os.environ.get('TWILIO_PHONE_NUMBER', None)

URL = 'https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json'.format(ACCOUNT)

def twilio_message_res(json, status):
    if status == 400:
        return {
            'error_code': json.get('code', None),
            'error_message': json.get('message', None)    
        }

    return  {
        'message_sid': json.get('sid', None),
        'status': json.get('status', None),
        'to': json.get('to', None),
        'body': json.get('body', None),
        'error_code': json.get('error_code', None),
        'error_message': json.get('error_message', None)
    }

@app.route('/sms/send', methods=['POST'])
@cross_origin(origin='*')
def send_sms():
    data = request.json
    telenum = data.get('to', None)
    message = data.get('message', None)
    
    if not telenum or not message:
        status = 400
        error = {
            'error': 'request Body does not contain required parameters',
            'status': status
        }
        return jsonify(error), status

    body = {
        'From': FROM,
        'To': telenum,
        'Body': (message),
    }
    res = requests.post(URL, data=body, auth=(ACCOUNT, TOKEN))
    return twilio_message_res(res.json(), res.status_code), res.status_code
    

if __name__ == '__main__':
    if not (ACCOUNT or TOKEN or FROM):
        raise EnvironmentError("Environment variables are ALL required")

    app.run(debug=True, host='0.0.0.0')
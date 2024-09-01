from flask import Flask, jsonify, request,Response
import requests
import os
from models import models
app = Flask(__name__)
accountid = os.getenv('ACCOUNTID')
print(f"Account ID: {accountid}")


@app.route('/v1/models', methods=['GET'])
def get_models():
    return jsonify(models)

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    cf_url = f"https://api.cloudflare.com/client/v4/accounts/{accountid}/ai/{path}"
    headers = dict(request.headers)
    body = request.get_json(silent=True) if request.is_json else request.data.decode('utf-8')

    # Print details to console
    print(f"URL: {cf_url}")
    print(f"Headers received: {headers}")
    print(f"Body received: {body}")

    # Make an external API request
    method = request.method
    headers = {
    "Authorization": headers["Authorization"],
    "Content-Type": "application/json"
    }
    try:
        if method == 'GET':
            external_response = requests.get(cf_url, headers=headers, params=request.args)
        elif method == 'POST':
            external_response = requests.post(cf_url, headers=headers, json=body)
        elif method == 'PUT':
            external_response = requests.put(cf_url, headers=headers, json=body)
        elif method == 'DELETE':
            external_response = requests.delete(cf_url, headers=headers, json=body)
        else:
            return jsonify({"error": "Unsupported HTTP method"}), 405
        response = Response(
            response=external_response.content,
            status=external_response.status_code,
            content_type=external_response.headers['Content-Type']
        )
        # Return the external response
        return response
    except Exception as e:
        print(f"Error during external API request: {e}")
        return jsonify({"error": "Failed to make external API request"}), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5050)
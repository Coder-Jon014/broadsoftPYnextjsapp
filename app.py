from flask import Flask, jsonify, request
from broadworks_ocip import BroadworksAPI
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

app = Flask(__name__)

# Create a global instance of BroadworksAPI
api = BroadworksAPI(
    host=os.getenv('API_HOST'),
    port=int(os.getenv('API_PORT')),
    username=os.getenv('API_USERNAME'),
    password=os.getenv('API_PASSWORD')
)

@app.route('/call-logs')
def get_call_logs():
    # Run the command
    user_id = request.args.get('user_id')
    response = api.command('UserBasicCallLogsGetListRequest', user_id=user_id)
    
    # Handle the response and return as JSON
    missed_calls = getattr(response, 'missed', [])
    received_calls = getattr(response, 'received', [])
    
    return jsonify({
        'missed_calls': [{'name': call.name, 'phone_number': call.phone_number, 'time': call.time} for call in missed_calls],
        'received_calls': [{'name': call.name, 'phone_number': call.phone_number, 'time': call.time} for call in received_calls]
    })

@app.route('/system-version')
def get_system_version():
    # Run the command
    response = api.command("SystemSoftwareVersionGetRequest")

    # Return the response as JSON
    return jsonify({
        'session_id': response.session_id,
        'version': response.version
    })

@app.route('/user-login-info')
def get_user_login_info():
    user_id = request.args.get('user_id')
    response = api.command("UserGetLoginInfoRequest", user_id=user_id)

    # Use the loop to get all attributes dynamically
    result = {}
    for attr in dir(response):
        if not attr.startswith('_') and not callable(getattr(response, attr)):
            value = getattr(response, attr)
            result[attr] = value

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
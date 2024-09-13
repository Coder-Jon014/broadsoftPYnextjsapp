from flask import Flask, jsonify, request
from broadworks_ocip import BroadworksAPI
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

app = Flask(__name__)

@app.route('/call-logs')
def get_call_logs():
    api = BroadworksAPI(
        host=os.getenv('API_HOST'),
        port=int(os.getenv('API_PORT')),
        username=os.getenv('API_USERNAME'),
        password=os.getenv('API_PASSWORD')
    )
    
    # Run the command
    user_id = request.args.get('user_id')
    response = api.command('UserBasicCallLogsGetListRequest', user_id=user_id)
    # response = api.command("SystemSoftwareVersionGetRequest")
    
    # Handle the response and return as JSON
    missed_calls = getattr(response, 'missed', [])
    received_calls = getattr(response, 'received', [])
    
    return jsonify({
        'missed_calls': [{'name': call.name, 'phone_number': call.phone_number, 'time': call.time} for call in missed_calls],
        'received_calls': [{'name': call.name, 'phone_number': call.phone_number, 'time': call.time} for call in received_calls]
    })

@app.route('/system-version')
def get_system_version():
    # Initialize Broadworks API with credentials from .env
    api = BroadworksAPI(
        host=os.getenv('API_HOST'),
        port=int(os.getenv('API_PORT')),
        username=os.getenv('API_USERNAME'),
        password=os.getenv('API_PASSWORD')
    )

    # Run the command
    response = api.command("SystemSoftwareVersionGetRequest")

    # Return the response as JSON
    return jsonify({
        'session_id': response.session_id,
        'version': response.version
    })

@app.route('/user-login-info')
def get_user_login_info():
    # Initialize Broadworks API with credentials from .env
    api = BroadworksAPI(
        host=os.getenv('API_HOST'),
        port=int(os.getenv('API_PORT')),
        username=os.getenv('API_USERNAME'),
        password=os.getenv('API_PASSWORD')
    )

    # Run the command
    user_id = request.args.get('user_id')
    response = api.command("UserLoginInfoGetRequest", user_id=user_id)

    # Return the response as JSON
    return jsonify({
        'session_id': response.session_id,
        'login_type': response.login_type,
        'locale': response.locale,
        'encoding': response.encoding,
        'group_id': response.group_id,
        'service_provider_id': response.service_provider_id,
        'is_enterprise': response.is_enterprise,
        'password_expires_days': response.password_expires_days,
        'last_name': response.last_name,
        'first_name': response.first_name,
        'user_id': response.user_id,
        'phone_number': response.phone_number
    })


if __name__ == '__main__':
    app.run(debug=True)
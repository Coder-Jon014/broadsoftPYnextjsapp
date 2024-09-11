# from flask import Flask, jsonify
# from broadworks_ocip import BroadworksAPI
# import os
# from dotenv import load_dotenv

# # Load .env variables
# load_dotenv()

# app = Flask(__name__)

# @app.route('/api/call-logs')
# def get_call_logs():
#     api = BroadworksAPI(
#         host=os.getenv('API_HOST'),
#         port=int(os.getenv('API_PORT')),
#         username=os.getenv('API_USERNAME'),
#         password=os.getenv('API_PASSWORD')
#     )
    
#     response = api.command('UserBasicCallLogsGetListRequest', user_id="Oberlin_High_2101")
#     # response = api.command("SystemSoftwareVersionGetRequest")
    
#     # Handle the response and return as JSON
#     missed_calls = getattr(response, 'missed', [])
#     received_calls = getattr(response, 'received', [])
    
#     return jsonify({
#         'missed_calls': [{'name': call.name, 'phone_number': call.phone_number, 'time': call.time} for call in missed_calls],
#         'received_calls': [{'name': call.name, 'phone_number': call.phone_number, 'time': call.time} for call in received_calls]
#     })

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, jsonify
from broadworks_ocip import BroadworksAPI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

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
        response
    })

if __name__ == '__main__':
    app.run(debug=True)

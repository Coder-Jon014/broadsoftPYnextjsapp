#from broadworks_ocip import BroadworksAPI
#
#api = BroadworksAPI(
#  host='172.28.9.38',
#  port=2208,
#  username="JDCoombs",
#  password="Eu.8cbi!ZZ.tQ4M")
##client.login()
#
##response=client.search_user_by_number('2843933482')
##response = api.command("SystemSoftwareVersionGetRequest")
##print(response.version)
#
##response = api.command("ServiceProviderGetListRequest")
#
##for provider in response.service_provider_table:
##  print(provider.service_provider_id)
##print(response)
##client.logout()
#
##Good/Interesting APIs
##UserBroadWorksAnywhereAddPhoneNumberRequest
##UserCallPoliciesGetRequest17
##UserBasicCallLogsGetListRequest
## How it is used- response = api.command("UserBasicCallLogsGetListRequest",user_id="Oberlin_High_2101")
##UserFeatureAccessCodeGetListRequest
## How it is- response = api.command("UserFeatureAccessCodeGetListRequest",user_id="Oberlin_High_2101")
##UserGetLoginInfoRequest
## How it is used- response = api.command("UserGetLoginInfoRequest",user_id="Oberlin_High_2101")
#
#response = api.command("UserGetRequest22", user_id="jon_danielhpbx")
#
#
#
#print(f"Response type: {type(response)}")
#print(f"Response: {(response)}")
#
#
#        
#        

#import time
#import logging
#import requests
#from requests.exceptions import RequestException
#from broadworks_ocip import BroadworksAPI
#
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)
#
#class CustomBroadworksAPI(BroadworksAPI):
#    def __init__(self, host, port, username, password):
#        super().__init__(host=host, port=port, username=username, password=password)
#        self.sessionId = str(int(round(time.time() * 1000)))
#
#    def _get_request_head(self, command):
#        head = f"""<?xml version="1.0" encoding="UTF-8"?>
#                  <soapenv:Envelope
#                  xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
#                  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
#                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
#                  <soapenv:Body>
#                  <processOCIMessage soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
#                  <arg0 xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">
#                  &lt;BroadsoftDocument protocol=&quot;OCI&quot; xmlns=&quot;C&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot;&gt;
#                  &lt;sessionId xmlns=&quot;&quot;&gt;{self.sessionId}&lt;/sessionId&gt;
#                  &lt;command xsi:type=&quot;{command}&quot; xmlns=&quot;&quot;&gt;
#               """
#        return head
#
#    def _get_request_tail(self):
#        tail = """&lt;/command&gt;
#                  &lt;/BroadsoftDocument&gt;
#                  </arg0>
#                  </processOCIMessage>
#                  </soapenv:Body>
#                  </soapenv:Envelope>
#               """
#        return tail
#
#    def _generate_request_body(self, command, req):
#        body = self._get_request_head(command) + req + self._get_request_tail()
#        return body
#    
#    def UserGetRequest20(self, user_id):
#        logger.info(f"Sending request to BWKS to GET User {user_id}")
#        reqst = """
#        <userId>""" + user_id + """</userId>
#        """
#        req = reqst.replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;")
#        request = self._generate_request_body("UserGetRequest20", req)
#        response = self.__send_request(request)
#        return response
#
#    def UserGetRequest22(self, user_id):
#        logger.info(f"Sending request to BWKS to GET User {user_id}")
#        reqst = f"""
#        <userId>{user_id}</userId>
#        """
#        req = reqst.replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;")
#        request = self._generate_request_body("UserGetRequest22", req)
#        response = self._send_request(request)
#        return response
#
#    def _send_request(self, request):
#      logger.info("Sending request to server")
#      headers = {'Content-Type': 'text/xml; charset=utf-8'}
#      url = f"http://{self.host}:{self.port}/webservice/services/ProvisioningService"
#      try:
#          logger.info(f"Request URL: {url}")
#          logger.info(f"Request headers: {headers}")
#          logger.info(f"Request body: {request[:500]}...")  # Print first 500 characters of request
#          response = requests.post(url, data=request, headers=headers, timeout=60)
#          response.raise_for_status()
#          logger.info("Received response from server")
#          logger.info(f"Response status code: {response.status_code}")
#          logger.info(f"Response headers: {response.headers}")
#          return response.text
#      except requests.Timeout:
#          logger.error("The request timed out")
#      except requests.ConnectionError:
#          logger.error("A connection error occurred")
#      except requests.RequestException as e:
#          logger.error(f"An error occurred: {e}")
#      return None
#
## Create an instance of the custom API class
#api = CustomBroadworksAPI(
#    host='172.28.9.38',
#    port=2208,
#    username="JDCoombs",
#    password="Eu.8cbi!ZZ.tQ4M"
#)
#
## Use the custom method to get the user information
#logger.info("Starting UserGetRequest22")
#response = api.UserGetRequest22(user_id="Oberlin_High_2101")
#
## Output the type and response content
#if response is not None:
#    logger.info(f"Response type: {type(response)}")
#    logger.info(f"Response: {response[:200]}...")  # Print first 200 characters
#else:
#    logger.error("No response received")
#
#logger.info("Script completed")



import re
from broadworks_ocip import BroadworksAPI

class CustomBroadworksAPI(BroadworksAPI):
    def receive_response(self):
        # Receive the raw XML response
        content = super().receive_response()
        
        # Replace invalid field names, e.g., replace 'line/port' with 'line_port'
        sanitized_content = re.sub(r'line/port', 'line_port', content)
        
        # Pass the sanitized XML response to the original XML decoding function
        return self.decode_xml(sanitized_content)

# Use the custom class
api = CustomBroadworksAPI(
    host='172.28.9.38',
    port=2208,
    username="JDCoombs",
    password="Eu.8cbi!ZZ.tQ4M"
)

response = api.command('UserGetRegistrationListRequest', user_id="Oberlin_High_2101")

# Print response attributes
print("Response attributes:")
for attr in dir(response):
    if not attr.startswith('_') and not callable(getattr(response, attr)):
        value = getattr(response, attr)
        if value is not None:
            print(f"{attr}: {value}")
        else:
            print(f"{attr}: None")


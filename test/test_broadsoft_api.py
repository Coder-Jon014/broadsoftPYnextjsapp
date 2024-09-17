from broadworks_ocip import BroadworksAPI

api = BroadworksAPI(
    host='172.28.9.38',
    port=2208,
    username="JDCoombs",
    password="Eu.8cbi!ZZ.tQ4M"
)

#response = api.command("SystemSoftwareVersionGetRequest")
#print(response)

response = api.command('UserGetLoginInfoRequest', user_id="Oberlin_High_2101")
print(response)

# python test_broadsoft_api.py
# UserGetLoginInfoResponse(session_id='8625bd77-f2ed-408a-89f4-3f59a7ee858c', login_type='User', locale='en_US', encoding='ISO-8859-1', group_id='JAM_Oberlin_High_School', service_provider_id='JAM_HPBX', is_enterprise=False, password_expires_days=-2147483648, last_name='James', first_name='Yvonne', user_id='Oberlin_High_2101@voip.digicelgroup.com', phone_number=None)


## Print each attribute, avoiding NoneType issues
#print("Response attributes:")
#for attr in dir(response):
#    if not attr.startswith('_') and not callable(getattr(response, attr)):
#        value = getattr(response, attr)
#        if value is not None:
#            print(f"{attr}: {value}")
#        else:
#            print(f"{attr}: None")

###UserFeatureAccessCodeGetListRequest
#Feature Access Codes
# Access the feature_access_code attribute and print it in a list format
#if hasattr(response, 'feature_access_code'):
#    feature_access_codes = getattr(response, 'feature_access_code', [])
#    print("Feature Access Codes:")
#    for fac in feature_access_codes:
#        print(f"Feature Name: {fac.feature_access_code_name}")
#        print(f"  Main Code: {fac.main_code}")
#        if fac.alternate_code:
#            print(f"  Alternate Code: {fac.alternate_code}")
#        print() 
#else:
#    print("No feature_access_code found in response.")


###UserBasicCallLogsGetListRequest
##Missed Calls
#if hasattr(response, 'missed'):
#    missed_calls = getattr(response, 'missed', [])
#    print("Missed Calls:")
#    for call in missed_calls:
#        print(f"Name: {call.name}")
#        print(f"Phone Number: {call.phone_number}")
#        print(f"Time: {call.time}")
#        print()  # Blank line for better readability
#else:
#    print("No missed calls found in response.")
#    
##Recieved Calls
#if hasattr(response, 'received'):
#    received_calls = getattr(response, 'received', [])
#    print("Received Calls:")
#    for call in received_calls:
#        print(f"Name: {call.name}")
#        print(f"Phone Number: {call.phone_number}")
#        print(f"Time: {call.time}")
#        print()  # Blank line for better readability
#else:
#    print("No received calls found in response.")


###UserGetRegistrationListRequest

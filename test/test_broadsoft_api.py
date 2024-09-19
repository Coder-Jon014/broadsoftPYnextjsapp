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
# print(response)


## Print each attribute, avoiding NoneType issues
print("Response attributes:")
for attr in dir(response):
   if not attr.startswith('_') and not callable(getattr(response, attr)):
       value = getattr(response, attr)
       if value is not None:
           print(f"{attr}: {value}")
       else:
           print(f"{attr}: None")


# [root@coe-voip Broadsoft]# python test_broadsoft_api.py
# Response attributes:
# encoding: ISO-8859-1
# first_name: Yvonne
# group_id: JAM_Oberlin_High_School
# is_enterprise: False
# last_name: James
# locale: en_US
# login_type: User
# password_expires_days: -2147483648
# phone_number: None
# service_provider_id: JAM_HPBX
# session_id: 1542c89a-f0ce-46a9-8e7b-375f30eb85d8
# type_: UserGetLoginInfoResponse
# user_id: Oberlin_High_2101@voip.digicelgroup.com

# Function:UserGetRequest22
# Response attributes:
# access_device_endpoint: AccessDeviceMultipleIdentityAndContactEndpointRead(access_device={'device_level': 'Group', 'device_name': 'Oberlin_High_2101'}, line_port='Oberlin_High_2101@voip.digicelgroup.com', private_identity=None, contact=[], static_registration_capable=False, use_domain=True, port_number=None, support_visual_device_management=False)
# address: None
# address_location: None
# alias: []
# alternate_user_id: []
# calling_line_id_first_name: Yvonne
# calling_line_id_last_name: James
# calling_line_id_phone_number: 8766199888
# country_code: 1
# default_alias: Oberlin_High_2101@voip.digicelgroup.com
# department: None
# department_full_path: None
# email_address: None
# extension: 201
# first_name: Yvonne
# group_id: JAM_Oberlin_High_School
# hiragana_first_name: Yvonne
# hiragana_last_name: James
# imp_id: None
# language: English
# last_name: James
# mobile_phone_number: None
# name_dialing_name: NameDialingName(name_dialing_last_name='James', name_dialing_first_name='Yvonne')
# national_prefix: None
# network_class_of_service: FraudBlk
# office_zone_name: None
# pager_phone_number: None
# phone_number: None
# primary_zone_name: None
# service_provider_id: JAM_HPBX
# session_id: 1388c2f8-affc-4ea2-ba05-023d15ba81b6
# time_zone: America/New_York
# time_zone_display_name: (GMT-04:00) (US) Eastern Time
# title: None
# trunk_addressing: None
# type_: UserGetResponse22
# user_id: Oberlin_High_2101@voip.digicelgroup.com
# yahoo_id: None


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

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


#Function:UserGetListInGroupRequest
# Response attributes:
# session_id: a5972674-f950-4673-b61e-b6e310e00fde

# type_: UserGetListInGroupResponse

# user_table: [userTable(user_id='Oberlin_High_2101', last_name='James', first_name='Yvonne', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='James', hiragana_first_name='Yvonne', in_trunk_group='false', extension='201', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2103', last_name='Johnson', first_name='Geraldine', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Johnson', hiragana_first_name='Geraldine', in_trunk_group='false', extension='203', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2114', last_name='Smith', first_name='Mr', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Smith', hiragana_first_name='Mr', in_trunk_group='false', extension='214', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2102', last_name='Ivey', first_name='Mrs', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Ivey', hiragana_first_name='Mrs', in_trunk_group='false', extension='202', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2104', last_name='Williams', first_name='Mrs', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Williams', hiragana_first_name='Mrs', in_trunk_group='false', extension='204', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2105', last_name='Bedword', first_name='Shaunakay', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Bedword', hiragana_first_name='Shaunakay', in_trunk_group='false', extension='205', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2106', last_name='Gray', first_name='Ms', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Gray', hiragana_first_name='Ms', in_trunk_group='false', extension='206', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2107', last_name='Bryant', first_name='Sybil', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Bryant', hiragana_first_name='Sybil', in_trunk_group='false', extension='207', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2108', last_name='Station', first_name='Nurse', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Station', hiragana_first_name='Nurse', in_trunk_group='false', extension='208', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2109', last_name='Walker', first_name='Mr. E', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Walker', hiragana_first_name='Mr. E', in_trunk_group='false', extension='209', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2110', last_name='Office', first_name='Security', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Office', hiragana_first_name='Security', in_trunk_group='false', extension='210', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2111', last_name='Spencer', first_name='Michelle', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Spencer', hiragana_first_name='Michelle', in_trunk_group='false', extension='211', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2112', last_name='Hunter', first_name='Ferron', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Hunter', hiragana_first_name='Ferron', in_trunk_group='false', extension='212', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2113', last_name='Office', first_name='Guidance', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Office', hiragana_first_name='Guidance', in_trunk_group='false', extension='213', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2115', last_name='Staffroom', first_name='Main', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Staffroom', hiragana_first_name='Main', in_trunk_group='false', extension='215', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2116', last_name='Office', first_name='Dean', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Office', hiragana_first_name='Dean', in_trunk_group='false', extension='216', country_code=None, national_prefix=None), userTable(user_id='Oberlin_High_2117', last_name='Area', first_name='Canteen', department=None, phone_number=None, phone_number_activated=None, email_address=None, hiragana_last_name='Area', hiragana_first_name='Canteen', in_trunk_group='false', extension='217', country_code=None, national_prefix=None)]


# Function:UserDevicePoliciesGetResponse21
# enable_acd: False
# enable_call_decline: False
# enable_call_forwarding_always: False
# enable_call_forwarding_busy: False
# enable_call_forwarding_no_answer: False
# enable_call_recording: False
# enable_device_feature_synchronization: True
# enable_dnd: False
# enable_executive: False
# enable_executive_assistant: False
# enable_security_classification: False
# line_mode: Single User Private and Shared
# session_id: 0d32e6af-c425-4744-ae76-245b2dc177ca
# type_: UserDevicePoliciesGetResponse21


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

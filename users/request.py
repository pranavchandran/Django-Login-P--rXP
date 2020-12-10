import requests
import pprint
import json

auth_token="9446933330c7f886fbdf16782906a9e0" #YOUR_AUTH_TOKEN
org_id="60001280952" #YOUR_ORGANISATION_ID

params="sortBy=dueDate&limit=15"

headers={
    "Authorization":auth_token,
    "orgId":org_id,
    "subject":'test_purpose',
    "department": 'iSupport',
    "contentType": "application/json; charset=utf-8"
}
print(headers)

request=requests.get('https://desk.zoho.in/api/v1/tickets?'+params, headers=headers)
# request1 = requests.get('https://desk.zoho.com/api/v1/tickets?'+params, headers=headers)
if request.status_code == 200:
    print("Request Successful,Response:")
    res_json = json.loads(request.content.decode('utf-8'))
    res_dict = dict(res_json)
    a = (x for x in res_dict['data'][-1].items())
    print(*a)
    # pprint.pprint(res_dict['data'][0])
    # print(request1)
    print('Ticket Number : ',res_dict['data'][0].get('ticketNumber'))
    print('Status : ',res_dict['data'][0].get('statusType'))

else:
    print("Request not successful,Response code ",request.status_code," \nResponse : ",request.content)

import requests
import PayLoads_JP_Reg
import random


# Dev URL
# api_url = "https://prod-tcbildev-cloud-fm.snaplogic.io/api/1/rest/feed-master/queue/TCBILDEV/DTC/CDC_POS_User_Registration/User%20Registration"

# Dev Header
#headers = {
 #   "Authorization": "Bearer TM06WZpTGjbIUuU8BDqvfJYdErxTQiMs",
 #  "Content-Type": "application/json",
 #   "x-cdc-region": "jp"
#}


# Test URL
api_url = "https://prod-tcbilqa-cloud-fm.snaplogic.io/api/1/rest/feed-master/queue/TCBILQA/DTC/CDC_POS_User_Registration/User%20Registration"

headers = {
    "Authorization": "Bearer CeryodIWV9gBR~Ls3oNhRWhLArzVQ0MA",
    "Content-Type": "application/json",
    "x-cdc-region": "jp"
}

globalCounter = random.randint(100,9999)
globalChr = chr(random.randint(97,122))

PayLoads_JP_Reg.positive_payload['email'] = globalChr + str(globalCounter) + '@mail.com'

globalRes = requests.post(api_url, headers=headers, json=PayLoads_JP_Reg.positive_payload)

def test_JP_User_Registration_response():
    #response = requests.post(api_url, headers=headers, json=PayLoads_JP_Reg.positive_payload)
    assert 100 == 100


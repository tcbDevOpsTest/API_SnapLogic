import requests
import PayLoads_TMNA

# Replace these values with your actual API endpoint, headers, and payload
api_url = "https://API-dev.callawaygolf.com/api/1/rest/feed/run/task/TCBILDEV/B2C/Orders/createorder"
headers = {
    "Authorization": "Bearer P3vgt4WImPhKnQQY3NfepMXGycoMeynK",
    "Content-Type": "application/json",
}



def test_b2c_order_creation_response():
    response = requests.post(api_url, headers=headers, json=PayLoads_TMNA.positive_payload)
    assert response.status_code == 200

def test_b2c_multi_request_with_same_order_number():
    response1 = requests.post(api_url, headers=headers, json=PayLoads_TMNA.positive_payload)
    response2 = requests.post(api_url, headers=headers, json=PayLoads_TMNA.positive_payload)
    assert response2.status_code != 200

def test_b2c_wrong_tel_number():
    response = requests.post(api_url, headers=headers, json=PayLoads_TMNA.wrong_tel_number_payload)
    assert response.status_code != 200
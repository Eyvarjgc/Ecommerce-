import requests


endpoint = 'http://localhost:8000/api2/'
# endpoint = 'http://localhost:8000/'

get_response = requests.get(endpoint, json={"product_id":123})
# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)
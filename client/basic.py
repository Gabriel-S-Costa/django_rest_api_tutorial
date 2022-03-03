from urllib import request
import requests

endpoint = "http://localhost:8000"

get_response = requests.get(endpoint) # HTTP request
print(get_response.text) # print raw text response

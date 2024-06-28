import key
import requests
import json

response = requests.get(url=key.URL_FORECAST)
data = json.loads(response.text)
print(data)

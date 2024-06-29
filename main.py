import key
import requests
from twilio.rest import Client

response = requests.get(url=key.URL_FORECAST, params=key.ow_params)
response.raise_for_status()
ow_data = response.json()

will_rain = False

for hour_data in ow_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <= 800:
        will_rain = True

if will_rain:
    client = Client(key.TW_ACCOUNT_SID, key.TW_AUTH)
    message = client.messages.create(from_=key.TW_PHONE,
                                     to=key.MY_OWN_PHONE,
                                     body="Rain coming!")
    print(message.sid)

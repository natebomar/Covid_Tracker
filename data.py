import requests
import json

# auth_url = 'https://api.covid19api.com/auth/subscriptions'
summary_url = 'https://api.covid19api.com/summary' 

# r_auth = requests.get(auth_url, auth = {"Email":"nate.bomar@gmail.com", "Subscription": "basic"})


payload={}
headers = {}

response = requests.request("GET", summary_url, headers=headers, data=payload)
data = response.json()
Countries = data["Countries"]
# print(Countries[8])
United_States = {}
for country in Countries:
    for (key, value) in country.items():
        if value == "US":
            United_States = country
print(United_States)



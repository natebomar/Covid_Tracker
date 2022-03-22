import requests
import firebase_admin
from firebase_admin import db
import json


#FireBase setup
cred_obj = firebase_admin.credentials.Certificate('covidtrack_key.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://covid-track-45cd7-default-rtdb.firebaseio.com/'
})


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
# print(United_States.items())

ref = db.reference("/")
ref.delete()

# print(data_to_html_table(United_States))
with open("us_summary.json", "w") as file:
    file.write(str(United_States).replace("'",'"'))

with open("us_summary.json", "r") as f:
    unordered = f.read().split(",")


with open("us_summary.json", "w") as order:
    for _ in unordered:
        order.write(_)
        if _ != unordered[len(unordered)-1]:
            order.write(",\n")

ref = db.reference("/")
with open("us_summary.json", "r") as file:
    current_sum = json.load(file)
ref.push(current_sum)
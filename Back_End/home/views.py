from django.shortcuts import render
from django.http import HttpResponse

import requests
# import firebase_admin
# from firebase_admin import db
import json
import urllib.request
# Create your views here.
# request --> response
# request handler, user does not see what is here


# API Link setup
summary_url = 'https://api.covid19api.com/summary' 
payload={}
headers = {}
big_sum = requests.request("GET", summary_url, headers=headers, data=payload)
def us_sum(request):
    data = big_sum.json()
    Countries = data["Countries"]
    United_States = {}
    for country in Countries:
        for (key, value) in country.items():
            if value == "US":
                United_States = country
    return render(request, 'test.html', {'summary': United_States})
from django.shortcuts import render
from django.http import HttpResponse

import requests
import json
import urllib.request
# Create your views here.
# request --> response
# request handler, user does not see what is here


# US Postman API Link setup
summary_url = 'https://api.covid19api.com/summary' 
payload={}
headers = {}
big_sum = requests.request("GET", summary_url, headers=headers, data=payload)


# LA County API Link setup
LA_url = 'https://data.chhs.ca.gov/api/3/action/datastore_search?resource_id=046cdd2b-31e5-4d34-9ed3-b48cdbc4be7a&limit=100000&q=los_angeles'  
fileobj = urllib.request.urlopen(LA_url)
response_dict = json.loads(fileobj.read())

# Home Page US table
# TODO: Add in LA table to home. Work with AD to figure out what should be here
# TODO: Really lay out what should be displayed on each page.
def us_sum(request):
    data = big_sum.json()
    Countries = data["Countries"]
    United_States = {}
    for country in Countries:
        for (key, value) in country.items():
            if value == "US":
                United_States = country

    return render(request, 'index.html', {
        "Region" : "United States of America",
        "New_Confirmed" : United_States["NewConfirmed"],
        "Total_Confirmed" : United_States["TotalConfirmed"],
        "New_Deaths" : United_States["NewDeaths"],
        "Total_Deaths" : United_States["TotalDeaths"],
        "Date" : United_States["Date"]
        })


#today html page --> LA ONLY
def us_today(request):
    for day in reversed(response_dict["result"]["records"]):
        if type(day["date"]) == str:
            most_recent = day

    return render(request, 'today.html',{
        "Date": most_recent["date"],
        "Region" : "Los Angeles County",
        "Today's Cases" : most_recent["reported_cases"],
        "Today's Deaths" : most_recent["deaths"],
        "Today's Tests" : most_recent["reported_tests"]
    })

def us_week(request):
    # data = big_sum.json()
    # Countries = data["Countries"]
    # United_States = {}
    # for country in Countries:
    #     for (key, value) in country.items():
    #         if value == "US":
    #             United_States = country
    return render(request, 'week.html')

#month html page
def us_month(request):
    # data = big_sum.json()
    # Countries = data["Countries"]
    # United_States = {}
    # for country in Countries:
    #     for (key, value) in country.items():
    #         if value == "US":
    #             United_States = country
    return render(request, 'month.html')


def us_alltime(request):
    # data = big_sum.json()
    # Countries = data["Countries"]
    # United_States = {}
    # for country in Countries:
    #     for (key, value) in country.items():
    #         if value == "US":
    #             United_States = country
    return render(request, 'alltime.html')

def us_vaccination(request):
    # data = big_sum.json()
    # Countries = data["Countries"]
    # United_States = {}
    # for country in Countries:
    #     for (key, value) in country.items():
    #         if value == "US":
    #             United_States = country
    return render(request, 'vaccination.html')


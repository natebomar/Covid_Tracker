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

# US Data(Postman)
data = big_sum.json()
Countries = data["Countries"]
United_States = {}
for country in Countries:
    for (key, value) in country.items():
        if value == "US":
            United_States = country

# LA Data 1 Day
for day in response_dict["result"]["records"]:
    if type(day["date"]) == str:
        most_recent = day


# Home Page US table
# TODO: Really lay out what should be displayed on each page.
def summary(request):
    return render(request, 'index.html', {
        "Region_1" : "United States of America",
        "New_Confirmed_1" : "{:,}".format(United_States["NewConfirmed"]),
        "Total_Confirmed_1" : "{:,}".format(United_States["TotalConfirmed"]),
        "New_Deaths_1" : "{:,}".format(United_States["NewDeaths"]),
        "Total_Deaths_1" : "{:,}".format(United_States["TotalDeaths"]),
        # "Date" : United_States["Date"],
        "Region_2" : "Los Angeles County",
        "New_Confirmed_2" : "{:,}".format(int(float(most_recent["reported_cases"]))),
        "Total_Confirmed_2" : "{:,}".format(int(float(most_recent["cumulative_cases"]))),
        "New_Deaths_2" : "{:,}".format(int(float(most_recent["deaths"]))),
        "Total_Deaths_2" : "{:,}".format(int(float(most_recent["cumulative_deaths"])))
    })



#today html page --> LA ONLY
def day(request):
    
    return render(request, 'day.html')

def week(request):
    return render(request, 'week.html', {
        "Date": most_recent["date"],
        "Region" : "Los Angeles County",
        "Week_Cases" : "{:,}".format(int(float(most_recent["reported_cases"]))),
        "Week_Deaths" : "{:,}".format(int(float(most_recent["deaths"]))),
        "Week_Tests" : "{:,}".format(int(float(most_recent["reported_tests"])))
    })

#month html page
def month(request):

    return render(request, 'month.html')


def alltime(request):
    return render(request, 'alltime.html', {
        "Region" : "United States of America",
        "Total_Confirmed" : "{:,}".format(United_States["TotalConfirmed"]),
        "Total_Deaths" : "{:,}".format(United_States["TotalDeaths"]),
        "Total_Confirmed_2" : "{:,}".format(int(float(most_recent["cumulative_cases"]))),
        "Total_Deaths_2" : "{:,}".format(int(float(most_recent["cumulative_deaths"])))
    })

def vaccination(request):
    # data = big_sum.json()
    # Countries = data["Countries"]
    # United_States = {}
    # for country in Countries:
    #     for (key, value) in country.items():
    #         if value == "US":
    #             United_States = country
    return render(request, 'vaccination.html')


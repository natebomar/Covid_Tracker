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
        
    Formatted = {
        "Region" : "United States of America",
        "New_Confirmed" : United_States["NewConfirmed"],
        "Total_Confirmed" : United_States["TotalConfirmed"],
        "New_Deaths" : United_States["NewDeaths"],
        "Total_Deaths" : United_States["TotalDeaths"],
        "Date" : United_States["Date"]
    }
    return render(request, 'index.html', {
        "Region": Formatted["Region"],
        "New_Confirmed" : Formatted["New_Confirmed"],
        "Total_Confirmed" : Formatted["Total_Confirmed"],
        "New_Deaths" : Formatted["New_Deaths"],
        "Total_Deaths" : Formatted["Total_Deaths"]
        })

# def us_region(request):
#     return render(request, 'index.html', {'Region': Formatted["Region"]})

# def us_newCon(request):
#     return render(request, 'index.html', {'New_Confirmed': Formatted['New_Confirmed']})

# def us_totalCon(request):
#     return render(request, 'index.html', {'Total_Confirmed': Formatted["Total_Confirmed"]})        

# def us_newDeaths(request):
#     return render(request, 'index.html', {'New_Deaths': str(Formatted["New_Deaths"])})

# def us_totalDeaths(request):
#     return render(request, 'index.html', {'Total_Deaths': str(Formatted["Total_Deaths"])})


#today html page
def us_today(request):
    # data = big_sum.json()
    # Countries = data["Countries"]
    # United_States = {}
    # for country in Countries:
    #     for (key, value) in country.items():
    #         if value == "US":
    #             United_States = country
    return render(request, 'today.html')

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
    data = big_sum.json()
    Countries = data["Countries"]
    United_States = {}
    for country in Countries:
        for (key, value) in country.items():
            if value == "US":
                United_States = country
        
    Formatted = {
        "Region" : "United States of America",
        "Total_Confirmed" : United_States["TotalConfirmed"],
        "Total_Deaths" : United_States["TotalDeaths"],
        "Date" : United_States["Date"]
    }
    return render(request, 'alltime.html', {
        "Region": Formatted["Region"],
        "Total_Confirmed" : Formatted["Total_Confirmed"],
        "Total_Deaths" : Formatted["Total_Deaths"],
        "Date": Formatted["Date"]
    })

def us_vaccination(request):
    # data = big_sum.json()
    # Countries = data["Countries"]
    # United_States = {}
    # for country in Countries:
    #     for (key, value) in country.items():
    #         if value == "US":
    #             United_States = country
    return render(request, 'vaccination.html')


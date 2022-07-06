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


# La Crescenta Vaccine API Link setup
url_91214 = "https://data.chhs.ca.gov/api/3/action/datastore_search?resource_id=ec32eece-7474-4488-87f0-6e91cb577458&q=91214"
url_91020 = "https://data.chhs.ca.gov/api/3/action/datastore_search?resource_id=ec32eece-7474-4488-87f0-6e91cb577458&q=91020"
fileobj_91214 = urllib.request.urlopen(url_91214)
fileobj_91020 = urllib.request.urlopen(url_91020)
dict_91214 = json.loads(fileobj_91214.read())
dict_91020 = json.loads(fileobj_91020.read())

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
last_index = response_dict["result"]["records"].index(most_recent)
# LA Data 1 Week
recent_week = response_dict["result"]["records"][-8:last_index+1]
weekly_cases = 0
weekly_deaths = 0 
weekly_tests = 0
for day in recent_week:
    weekly_cases += abs(int(float(day["reported_cases"])))
    weekly_deaths += abs(int(float(day["reported_deaths"])))
    if type(day["reported_tests"]) == str:
        weekly_tests += abs(int(float(day["reported_tests"])))

# LA Data 1 month
recent_month = response_dict["result"]["records"][-31:last_index+1]
monthly_cases = 0
monthly_deaths = 0 
monthly_tests = 0
for day in recent_month:
    monthly_cases += abs(int(float(day["reported_cases"])))
    monthly_deaths += abs(int(float(day["reported_deaths"])))
    if type(day["reported_tests"]) == str:
        monthly_tests += abs(int(float(day["reported_tests"])))


# VACCINE DATA

# 91214
for week in dict_91214["result"]["records"]:
    vac_912 = week

full_per_912 = int(100 * float(vac_912["percent_of_population_fully_vaccinated"])+.5)
full_num_912 = int(float(vac_912["persons_fully_vaccinated"]))
part_per_912 = int(100 * (float(vac_912["percent_of_population_partially_vaccinated"]))+.5)
part_num_912 = int(float(vac_912["persons_partially_vaccinated"]))
boost_per_912 = int(100 * (float(vac_912["booster_recip_count"] ) / float(vac_912["age5_plus_population"]))+.5)
boost_num_912 = int(float(vac_912["booster_recip_count"]))
# 91020
for week in dict_91020["result"]["records"]:
    vac_910 = week

full_per_910 = int(100 * (float(vac_910["percent_of_population_fully_vaccinated"]))+.5)
full_num_910 = int(float(vac_910["persons_fully_vaccinated"]))
part_per_910 = int(100 * (float(vac_910["percent_of_population_partially_vaccinated"]))+.5)
part_num_910 = int(float(vac_910["persons_partially_vaccinated"]))
boost_per_910 = int(100 * (float(vac_910["booster_recip_count"] ) / float(vac_910["age5_plus_population"]))+.5)
boost_num_910 = int(float(vac_910["booster_recip_count"]))
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
        "New_Confirmed_2" : "{:,}".format(abs(int(float(most_recent["reported_cases"])))),
        "Total_Confirmed_2" : "{:,}".format(abs(int(float(most_recent["cumulative_cases"])))),
        "New_Deaths_2" : "{:,}".format(abs(int(float(most_recent["reported_deaths"])))),
        "Total_Deaths_2" : "{:,}".format(abs(int(float(most_recent["cumulative_deaths"]))))
    })

#today html page --> LA ONLY
def day(request):
   return render(request, 'day.html', {
        "Date": most_recent["date"],
        "Region" : "Los Angeles County",
        "Day_Cases" : "{:,}".format(int(float(most_recent["reported_cases"]))),
        "Day_Deaths" : "{:,}".format(int(float(most_recent["reported_deaths"]))),
        "Day_Tests" : "{:,}".format(int(float(most_recent["reported_tests"])))
    })
def week(request):
    return render(request, 'week.html', {
        "Start_Date": recent_week[0]["date"],
        "End_Date": recent_week[-1]["date"],
        "Region" : "Los Angeles County",
        "Week_Cases" : "{:,}".format(weekly_cases),
        "Week_Deaths" : "{:,}".format(weekly_deaths),
        "Week_Tests" : "{:,}".format(weekly_tests)
    })

#month html page
def month(request):

    return render(request, 'month.html', {
        "Start_Date": recent_month[0]["date"],
        "End_Date": recent_month[-1]["date"],
        "Region" : "Los Angeles County",
        "Month_Cases" : "{:,}".format(monthly_cases),
        "Month_Deaths" : "{:,}".format(monthly_deaths),
        "Month_Tests" : "{:,}".format(monthly_tests)
    })


def alltime(request):
    return render(request, 'alltime.html', {
        "Region" : "United States of America",
        "Total_Confirmed" : "{:,}".format(United_States["TotalConfirmed"]),
        "Total_Deaths" : "{:,}".format(United_States["TotalDeaths"]),
        "Total_Confirmed_2" : "{:,}".format(abs(int(float(most_recent["cumulative_cases"])))),
        "Total_Deaths_2" : "{:,}".format(abs(int(float(most_recent["cumulative_deaths"]))))
    })

def vaccination(request):
    return render(request, 'vaccination.html',{
        "Region_1" : "91214",
        "91214_full_percent" :  "{:,}".format(full_per_912),
        "91214_full_num" : "{:,}".format(full_num_912),
        "91214_part_percent" : "{:,}".format(part_per_912),
        "91214_part_num" : "{:,}".format(part_num_912),
        "91214_boost_percent" : "{:,}".format(boost_per_912),
        "91214_boost_num" : "{:,}".format(boost_num_912),
        "Region_2": "91020",
        "91020_full_percent" : "{:,}".format(full_per_910),
        "91020_full_num" : "{:,}".format(full_num_910),
        "91020_part_percent" : "{:,}".format(part_per_910),
        "91020_part_num" : "{:,}".format(part_num_910),
        "91020_boost_percent" : "{:,}".format(boost_per_910),
        "91020_boost_num" : "{:,}".format(boost_num_910)
    })


import requests
import json
import urllib.request



# Covid 19 USA Setup
summary_url = 'https://api.covid19api.com/summary' 
payload={}
headers = {}
response = requests.request("GET", summary_url, headers=headers, data=payload)


# Covid 19 Los Angeles Setup
LA_url = 'https://data.chhs.ca.gov/api/3/action/datastore_search?resource_id=046cdd2b-31e5-4d34-9ed3-b48cdbc4be7a&limit=100000&q=los_angeles'  
fileobj = urllib.request.urlopen(LA_url)
response_dict = json.loads(fileobj.read())
# print(response_dict['result']['records'])
for day in reversed(response_dict["result"]["records"]):
    if type(day["date"]) == str:
        most_recent = day
# Keys for a given day are ass follows:
# 'rank', 'cumulative_reported_deaths', 'cumulative_deaths', 'cumulative_positive_tests', 'area', 
# 'cumulative_cases', 'reported_cases', 'positive_tests', 'cumulative_reported_cases', 'area_type', 
# 'reported_deaths', 'total_tests', 'deaths', 'reported_tests', 'date', 'cases', '_id', 
# 'cumulative_total_tests', 'population'

# Useful Keys: 
# 'cumulative_reported_deaths', 'cumulative_deaths', 'cumulative_positive_tests','cumulative_cases', 
# 'reported_cases', 'positive_tests', 'cumulative_reported_cases', 'reported_deaths', 'total_tests', 
# 'deaths', 'reported_tests', 'date', 'cumulative_total_tests', 'population'



# # Fetch US Summary
# data = response.json()
# Countries = data["Countries"]
# United_States = {}
# for country in Countries:
#     for (key, value) in country.items():
#         if value == "US":
#             United_States = country

# print(United_States.items())
# Formatted = {
#     "Region" : "United States of America",
#     "New Confirmed" : United_States["NewConfirmed"],
#     "Total Confirmed" : United_States["TotalConfirmed"],
#     "New Deaths" : United_States["NewDeaths"],
#     "Total Deaths" : United_States["TotalDeaths"],
#     "Date" : United_States["Date"]
# }
# print(Formatted)

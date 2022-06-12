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


# for day in response_dict["result"]["records"]:
#     if type(day["date"]) == str:
#         most_recent = day
# print(most_recent)
## Useful Keys: 
## 'cumulative_reported_deaths', 'cumulative_deaths', 'cumulative_positive_tests','cumulative_cases', 
## 'reported_cases', 'positive_tests', 'cumulative_reported_cases', 'reported_deaths', 'total_tests', 
## 'deaths', 'reported_tests', 'date', 'cumulative_total_tests', 'population'

# Vaccination in La Crescenta
url_91214 = "https://data.chhs.ca.gov/api/3/action/datastore_search?resource_id=ec32eece-7474-4488-87f0-6e91cb577458&q=91214"
url_91020 = "https://data.chhs.ca.gov/api/3/action/datastore_search?resource_id=ec32eece-7474-4488-87f0-6e91cb577458&q=91020"
fileobj_91214 = urllib.request.urlopen(url_91214)
fileobj_91020 = urllib.request.urlopen(url_91020)
dict_91214 = json.loads(fileobj_91214.read())
dict_91020 = json.loads(fileobj_91020.read())

# dict_keys(['persons_partially_vaccinated', 'vaccine_equity_metric_quartile', 
# 'percent_of_population_partially_vaccinated', 'persons_fully_vaccinated', 'local_health_jurisdiction', 
# 'percent_of_population_with_1_plus_dose', 'age12_plus_population', 'redacted', 'vem_source', 'rank', 
# 'county', 'as_of_date', 'booster_recip_count', 'zip_code_tabulation_area', '_id', 
# 'percent_of_population_fully_vaccinated', 'age5_plus_population'])

for week in dict_91214["result"]["records"]:
    most_recent = week

print(int(100 * (float(week["percent_of_population_fully_vaccinated"]))+.5))
import requests
import json
from configparser import ConfigParser

################# TESTs: #################

# API overview test #
api_call_overview = requests.get("{}/all".format("https://coronavirus-19-api.herokuapp.com"))
load_json_overview = json.loads(api_call_overview.text)

bool_overview = "cases" and "deaths" and "recovered" in load_json_overview

if bool_overview == True:
    print("OVERVIEW TEST: PASSED")
else:
    print("OVERVIEW TEST: FAILED")

# API country info test #
api_call_country = requests.get("{}/countries/china".format("https://coronavirus-19-api.herokuapp.com"))
load_json_country = json.loads(api_call_country.text)

bool_country = "country" and "active" and "critical" in load_json_country

if bool_country == True:
    print("COUNTRY INFO API TEST: PASSED")
else:
    print("COUNTRY INFO API TEST: FAILED")


# API COUNTRIES LIST TEST #
api_call_countries = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
load_json_countries = json.loads(api_call_countries.text)

countries = []

for x in load_json_countries: countries.append(x['country'])

bool_countries = "Iran" and "Switzerland" and "UK" and "Germany" in countries

if bool_countries == True:
    print("COUNTRIES NAMES API TEST: PASSED")
else:
    print("COUNTRIES NAMES API TEST: FAILED")

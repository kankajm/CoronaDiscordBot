import json
import requests

class api():
    # Gets data from api.
    # Returns global data in array
    def overview_corona():
        api_call = requests.get("https://coronavirus-19-api.herokuapp.com/all")
        load_json = json.loads(api_call.text)

        cases = load_json.get('cases')
        deaths = load_json.get('deaths')
        recovered = load_json.get('recovered')

        return [cases, deaths, recovered]


     # Gets data from API about one specific country. Output is array.
     # WARNING: It's important to change int to str when it's used.
    def country_corona(country):
        api_call = requests.get(" https://coronavirus-19-api.herokuapp.com/countries/{}".format(country))
        load_json = json.loads(api_call.text)

        country_name = load_json.get('country')
        cases = load_json.get('cases')
        today_cases = load_json.get('todayCases')
        deaths = load_json.get('deaths')
        today_deaths = load_json.get('todayDeaths')
        recovered_people = load_json.get('recovered')
        active_cases = load_json.get('active')
        critical_cases = load_json.get('critical')
        cases_per_one_million_citizens = load_json.get('casesPerOneMillion')
        deaths_per_one_million_citizens = load_json.get('deathsPerOneMillion')

        return [country_name, cases, today_cases, deaths, today_deaths, recovered_people, active_cases, critical_cases, cases_per_one_million_citizens, deaths_per_one_million_citizens]



# Tests --> PASSED
# print(api.overview_corona())
# print()
# print(api.country_corona("Slovakia"))
# print(api.country_corona("Italy"))
# print(api.country_corona("USA"))

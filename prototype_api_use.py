import json
import requests


api_call = requests.get("https://coronavirus-19-api.herokuapp.com/all")
load_json = json.loads(apiCall.text)

cases = loadJson.get('cases')
deaths = loadJson.get('deaths')
recovered = loadJson.get('recovered')

debug_message_json = "Clear JSON: {raw_json}"
debug_message_visible = "There's {number_of_cases} cases right now, {number_of_deaths} deaths and {number_of_recoveries} people recovered from the COVID-19."

print(debug_message_json.format(raw_json = str(loadJson)))
print(debug_message_visible.format(number_of_cases = str(cases), number_of_deaths = deaths, number_of_recoveries = recovered))


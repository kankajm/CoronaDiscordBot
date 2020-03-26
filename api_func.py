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



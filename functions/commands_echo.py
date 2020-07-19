from . import api
from . import misc_func

class commands:
    def getCzechPrefixes():
        return ['CZ', 'cz', 'czech', 'czechia', 'Czechia', 'Czech']

    def getCzechCoronaData():
        data = api.api_func.country_corona('Czechia')
        return "According to Ministry of Health of the Czech Republic, Czechia has tested {} people. To this date Czechia have {} cases, {} deaths and {} people recovered from the COVID-19. Today was detected {} cases and {} deaths. Source: http://tiny.cc/mzcr-covid, Ministerstvo zdravotnictví České republiky.".format(
            data[-2], data[1], data[3], data[5], data[2], data[4])

    def getGlobalCoronaData():
        data = api.api_func.overview_corona()
        return ", there's {} cases in a world right now, {} deaths and {} people recovered from the COVID-19.".format(data[0], data[1], data[2])

    def getInfoAboutCoronavirus():
        data_string = misc_func.symptoms_info()
        return ", {} Source: http://tiny.cc/WHOLINK , WHO.".format(data_string)

    def getInviteLinkMessage():
        return ", to invite this bot on your server use: https://shorturl.at/fprIN"

    def getKoreaFixedCoronaData():
        data = api.api_func.country_corona("S. Korea")
        data[0] = data[0].replace(" ", "")
        return ", {} has {} cases and {} deaths. Today there are {} cases and {} deaths. {} people recovered. They're still {} active cases and {} people are in critical condition. The concentration of cases in {} is {} cases per one milion citizens.".format(data[0], data[1], data[3], data[2], data[4], data[5], data[6], data[7], data[0], data[8])

    def getCountryCoronaData(args):
        data = api.api_func.country_corona(args)
        if data == "error":
            return ", you have written wrong country name or database is unavaible. Try it again."
        else:
            return ", {} has {} cases and {} deaths. Today there are {} cases and {} deaths. {} people recovered. They're still {} active cases and {} people are in critical condition. The concentration of cases in {} is {} cases per one milion citizens.".format(data[0], data[1], data[3], data[2], data[4], data[5], data[6], data[7], data[0], data[8])

    def getIgnoredArgs():
        return ['CZ', 'cz', 'czech', 'czechia', 'Czechia', 'Czech', 'S.Korea', 'version', 'servers', 'invite', 'ping', 'help', 'info', 'overview', 'world']

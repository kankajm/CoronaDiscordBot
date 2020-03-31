import requests
from bs4 import BeautifulSoup

def covid_scrap():
    zdroj_dat = "Ministerstvo zdravotnictví České republiky"
    zdroj_link = "https://onemocneni-aktualne.mzcr.cz/covid-19"
    pocet_testu = 0
    pocet_nemoc = 0
    pocet_uzdraven = 0
    pocet_mrtvy = 0
    data = requests.get('https://onemocneni-aktualne.mzcr.cz/covid-19')

    soup = BeautifulSoup(data.text, 'html.parser')

    # Najde počet provedených testů
    for x in soup.findAll(id="prehled"):
        pocet_testu = soup.find(id="count-test").text.replace(" ", "")

    # Najde počet nemocných
    for x in soup.findAll(id="prehled"):
        pocet_nemoc = soup.find(id="count-sick").text.replace(" ", "")

    # Najde počet uzdravených
    for x in soup.findAll(id="prehled"):
        pocet_uzdraven = soup.find(id="count-recover").text.replace(" ", "")

    # Najde počet úmrtí
    for x in soup.findAll(id="prehled"):
        pocet_mrtvy = soup.find(id="count-dead").text.replace(" ", "")

    scraped_data_list = [zdroj_dat, zdroj_link, pocet_testu, pocet_nemoc, pocet_uzdraven, pocet_mrtvy]

    return scraped_data_list

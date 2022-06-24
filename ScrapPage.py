import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content


soup = BeautifulSoup(page, "html.parser")


titres = soup.find_all("a", class_="gem-c-document-list__item-title")
titre_textes = []
for titre in titres:
	titre_textes.append(titre.string.encode("ascii", "ignore"))


descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
description_textes = []
for description in descriptions:
	description_textes.append(description.string.encode("ascii", "ignore"))

print(titre_textes)
print(description_textes)


def getDescriptionPage():
    return description_textes
def getTirePage():
    return titre_textes




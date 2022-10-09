import requests
import pandas as pd
from pandas import read_csv

apiKey = "b5db21fc04c6e10115d06180701edcf5"
url = "https://api.elsevier.com/content/search/scopus"

a = read_csv("acceptedInstance1.csv")

i = 0

array_citazioni = []

while i < 147:
    try:
        q = a.iloc[i]["TITLE"]
        print(q)
        params = {"query": q, "apiKey": apiKey, "start": 0, "count": 1}
        r = requests.get(url=url, params=params)
        data = r.json()
        data2 = data['search-results']['entry'][0]['dc:creator']
        print(data2)
        data3 = data['search-results']['entry'][0]['prism:publicationName']
        print(data3)

        i = i + 1
        citazione = "\n@book{Scopus \n title={" + a.iloc[i]["TITLE"] +" } \n author={"+data2+" } \n journal={"+data3+"} \n publisher={} \n }\n"
        array_citazioni.append(citazione)
    finally:
        i = i + 1
        continue
file = open("fileCitazioni1.txt", "w")

for x in array_citazioni:
    file.write(x)

file.close()
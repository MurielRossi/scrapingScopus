import requests
import pandas as pd
#include json library
import json
from numpy.ma import diff

q = "medicine"
apiKey = "b5db21fc04c6e10115d06180701edcf5"
url = "https://api.elsevier.com/content/search/scopus"
params = {"query": q, "apiKey": apiKey,"start": 0, "count": 25}

r = requests.get(url = url, params = params)
data = r.json()
print(data)
#df = pd.read_json(data)
data[2][0].to_csv('/home/muriel/PycharmProjects/pythonProject1/file.csv', sep=',')



import requests
import pandas as pd


q = "  ( ( ( medic*  OR  healthcare OR bioinformatic)  AND  ( ( artificial  AND intelligence )  OR  ( machine  AND learning ) ) ) )  AND  ( LIMIT-TO ( LANGUAGE ,  \"English\" ) AND ( LIMIT-TO ( SUBJAREA ,  \"MEDI\" ) ) AND ( LIMIT-TO ( SUBJAREA ,  \"BIOC\" ) ) AND ( LIMIT-TO ( SUBJAREA ,  \"COMP\" ) ) AND (  LIMIT-TO ( OA ,  \"all\" ) ) AND (EXCLUDE (DOCTYPE, \"cr\") ) AND (EXCLUDE (DOCTYPE, \"no\") ) AND (EXCLUDE (DOCTYPE, \"le\") ) AND (EXCLUDE (DOCTYPE, \"bk\") ) AND (EXCLUDE (DOCTYPE, \"sh\") ) )"

apiKey = "b5db21fc04c6e10115d06180701edcf5"
url = "https://api.elsevier.com/content/search/scopus"
i = 0
a = 0
while 1:
    params = {"query": q, "apiKey": apiKey, "start": i, "count": 25}

    r = requests.get(url = url, params = params)

    data = r.json()
    print(data)
    data2 = data['search-results']['entry']
    lista = []
    print(lista)
    for x in data2:
        lista.append({
            "TITLE": x['dc:title'],
            "ACCEPTED": "NO"
        })

    ciao = pd.DataFrame.from_records(lista)
    print(ciao)
    ciao.to_csv('/home/muriel/PycharmProjects/pythonProject1/file'+str(a), sep=',')
    i = i + 25
    a = a + 1




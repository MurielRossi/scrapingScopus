import glob

import pandas as pd
import PyPDF2

array_path = []

array_path = glob.glob("pdfTirocinio/*")
print(array_path)
e = 0
for x in array_path:
    print(x)
    pdfFileObj = open(x, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = len(pdfReader.pages)
    print(num_pages)
    lista = []
    lista.append({
        "TITLE": x,
        "CONTENT": ""
    })

    i = 0
    while i < num_pages:
        pageObj = pdfReader.getPage(i)
        page1 = pageObj.extractText()
        print(page1)
        lista[e]["CONTENT"] + page1

        i = i + 1

    ciao = pd.DataFrame.from_records(lista)
    print(ciao)
    ciao.to_csv('\pdfToCSV\p' + x, sep=',')
    e = e + 1

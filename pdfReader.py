import glob

import pandas as pd
import PyPDF2

array_path = []

array_path = glob.glob("pdfTirocinio/*")
print(array_path)
e = 0

for x in array_path:
    pdfFileObj = open(x, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = len(pdfReader.pages)
    print(num_pages)
    array = []
    lista = ""

    i = 0
    while i < num_pages:
        pageObj = pdfReader.getPage(i)
        page1 = pageObj.extractText()
        lista = lista + page1
        print(lista)

        i = i + 1

    array.append(lista)

    e = e + 1

ciao = []

i = 0
for x in array:
    ciao.append({
        "NUMBER": str(i),
        "CONTENT": x
    })

ciao = pd.DataFrame.from_records(array)
ciao.to_csv('/home/muriel/PycharmProjects/pythonProject1/pdfToCSV/myPDF.csv')


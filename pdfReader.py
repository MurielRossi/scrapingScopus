import glob
import time
from io import StringIO

import pandas as pd
import PyPDF2
import cleanFun


array_path = glob.glob("pdfTirocinio/*")
print(array_path)
open('pdfToCSV/myPDF.csv', 'w')

array = []

e = 0
for x in array_path:
    pdfFileObj = open(x, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = len(pdfReader.pages)
    print(num_pages)
    lista = ""
    i = 0
    while i < num_pages:
        pageObj = pdfReader.getPage(i)
        page1 = pageObj.extractText()
        lista = lista + " " + page1
        print(page1)
        i = i + 1

    array.append(lista)

    e = e + 1

ciao = pd.DataFrame(array)
print(ciao)
ciao.to_csv('/home/muriel/PycharmProjects/pythonProject1/pdfToCSV/myPDF.csv', sep=',')
start = time.time()
ciao[0] = ciao[0] \
    .apply(cleanFun.lower_converter) \
    .apply(cleanFun.break_remover) \
    .apply(cleanFun.punt_remover) \
    .apply(cleanFun.href_remover) \
    .apply(cleanFun.http_remover) \
    .apply(cleanFun.spaces_remover) \
    .apply(cleanFun.stopwords_remover) \
    .apply(cleanFun.lemmatizer) \
    .apply(cleanFun.exclude_not_english)
# .apply(cleanFun.word_correction)
# .apply(cleanFun.correct_words)\
end = time.time()
print(end - start)
ciao.to_csv('/home/muriel/PycharmProjects/pythonProject1/pdfToCSV/myPDFCleaned.csv', sep=',')

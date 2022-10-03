import pandas as pd
import PyPDF2

pdfFileObj = open('pdfTirocinio/A_machine_learning_COVID19_mass_screening_based_on_symptoms_and.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(i)
page1 = pageObj.extractText()
print(page1)
#df.to_csv("./test.csv")


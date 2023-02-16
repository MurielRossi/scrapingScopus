import json

import numpy
import openai
import pandas as pd
import os
import csv

#open the file of the response
f = open('answerResponse/response.csv', 'w')

#creating the writer
writer = csv.writer(f)


df = pd.read_csv('/home/muriel/PycharmProjects/pythonProject1/pdfToCSV/myPDFCleaned.csv')

openai.api_key_path = 'api_key'

index = 0
for i in df:
  text = df.loc[index].at["Content"]
  index = index + 1
  print(text)
  text = text + "\n\n" + "Human: Hello, who are you?" + "\nAI: I am an AI created by OpenAI. How can I help you today?" + "\nHuman: I'd like to cancel my subscription." "\nAI:"

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=text,
    temperature=0,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )


  print(response)

  writer.writerow(response)

f.close()
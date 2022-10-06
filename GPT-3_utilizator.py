import json

import jsonlines as jsonlines
import openai
import pandas as pd
import os

jsons = []
df = pd.read_csv('/home/muriel/PycharmProjects/pythonProject1/pdfToCSV/myPDF.csv')


def save_json(x):
    global jsons
    jsons.append({"text": x})


print(df.columns)

df = df["CONTNENT"].apply(save_json)
with jsonlines.open('/home/muriel/PycharmProjects/pythonProject1/jsonFIle/myfile.jsonl', 'w') as writer:
    writer.write_all(jsons)


#openai.api_key = os.getenv("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")
openai.api_key = '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'

start_sequence = "\nA:How IA is used?"
restart_sequence = "\n\nQ: "
response = openai.Completion.create(
    model="text-davinci-002",
    prompt="ciao uihytrgiuhrtgoiushrg biuehrfiu iuyaryeft uoyawegfr uyaehgf uyaehgf uyweghr jhasyedfb ayuheg wuyeghfr uywehgr oquyhwefr joyuwheg ow3uyjgr oyhwegr ",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
)

print(response)

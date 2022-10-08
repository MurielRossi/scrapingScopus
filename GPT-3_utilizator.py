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

start_sequence = "\nA:"
restart_sequence = "\n\nQ:"
testo  = "Introduction: Discriminating asthma from chronic obstructive pulmonary disease (COPD) using medico-administra-\ntive databases is challenging but necessary for medico-economic analyses focusing on respiratory diseases. Artifcial\n\nintelligence (AI) may improve dedicated algorithms.\nObjectives: To assess performance of diferent AI-based approaches to distinguish asthmatics from COPD patients\nin medico-administrative databases where the clinical diagnosis is absent. An “Asthma COPD Overlap” category was\ndefned to further test whether AI can detect complexity.\nMethods: This study included 178,962 patients treated by two “R03” treatment prescriptions at least from January\n\n2016 to December 2018 and managed by either a general practitioner and/or a pulmonologist participating in a per-\nmanent longitudinal observatory of prescription in ambulatory medicine (LPD). Clinical diagnoses are available in this\n\ndatabase and were used as gold standards to develop diagnostic rules. Three types of AI approaches were explored\nusing data restricted to demographics and treatment dispensations: multinomial regression, gradient boosting and\n\nrecurrent neural networks (RNN). The best performing model (based on metric properties) was then applied to esti-\nmate the size of asthma and COPD populations based on a database (LRx) of treatment dispensations between July,\n\n2018 and June, 2019.\n\nResults: The best models were obtained with the boosting approach and RNN, with an overall accuracy of 68%. Per-\nformance metrics were better for asthma than COPD. Based on LRx data, the extrapolated numbers of patients treated\n\nfor asthma and COPD in France were 3.7 and 1.2 million, respectively. Asthma patients were younger than COPD\npatients (mean, 49.9 vs. 72.1 years); COPD occurred mostly in men (68%) compared to asthma (33%).\nConclusion: AI can provide models with acceptable accuracy to distinguish between asthma, ACO and COPD in\nmedico-administrative databases where the clinical diagnosis is absent. Deep learning and machine learning (RNN)\nhad similar performances in this regard.\nKeywords: Algorithms, COPD, Chronic obstructive pulmonary disease, Asthma, ICD code, Epidemiology, Prevalence,\nHealthcare administrative databases\n\nQ: What methods of artificial intelligence have been used in this text?\n\nA: The methods of artificial intelligence used in this text include multinomial regression, gradient boosting, and recurrent neural networks.\n\nQ: How has artificial intelligence been applied in this text?"
response = openai.Completion.create(
    model="text-davinci-002",
    prompt= testo,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
)

print(start_sequence)

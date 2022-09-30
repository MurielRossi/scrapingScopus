import glob

import pandas as pd


array_path = []
open('concatCSV', 'w')
concatCSV = pd.DataFrame()

array_path = glob.glob("/home/muriel/PycharmProjects/pythonProject1/allCSV/*")
array_panda = []
for x in array_path:
    csv = pd.read_csv(x)
    array_panda.append(csv)
concatCSV = pd.concat(array_panda)

concatCSV.to_csv("./concat.csv")

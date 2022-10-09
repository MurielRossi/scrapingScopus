import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25
fig = plt.subplots(figsize=(30, 15))

# set height of bar
etichette_tecnologie = ["Baiesiano", "CNN", "NLP", "Classificazione", "Modello Logistico", "Reti neurali",
                        "Image Detection", "Regressione", "Deep Learning", "Reti Avversarie"]
tecnology = [1, 3, 2, 6, 1, 4, 4, 3, 5, 1]
etichette_usi = ["Predizioni Patologie", "Malattie Pediatriche", "Salute Mentale", "Studio Epidemie", "Neuropatie",
                 "Salute Dentale", "Ricerca sul Cancro", "Aspettative di vita", "Creazione Medicinali",
                 "Ausilio alla Diagnosi", "Analisi Prenatale"]
usi = [3, 1, 1, 2, 1, 1, 9, 2, 1, 11, 1]

# Set position of bar on X axis
br1 = np.arange(len(tecnology))
br2 = [x + barWidth for x in br1]

# Make the plot
plt.bar(br1, tecnology, color='m',
        edgecolor='black')

# Adding Xticks
plt.xlabel('Tecnologie', fontweight='bold', fontsize=15)
plt.ylabel('No. Utilizzi', fontweight='bold', fontsize=15)
plt.xticks([r for r in range(len(etichette_tecnologie))],
           etichette_tecnologie)

plt.legend()
plt.show()

# bar plot
plt.figure(figsize=(10, 5))
plt.bar(np.arange(len(usi)), height=usi, color="c", width=0.4)
plt.xlabel('Caso D\'uso', fontweight='bold', fontsize=15)
plt.ylabel('Riscontri', fontweight='bold', fontsize=15)
plt.xticks([r for r in range(len(etichette_usi))],
           etichette_usi)

plt.show()
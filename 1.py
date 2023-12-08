import csv
from matplotlib import pyplot as plt
import numpy as np

# Lecture des données de population pour 2021
communes_2021 = []
with open('donnees_2021.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        communes_2021.append(row)

communes_2021 = [[communes_2021[i + 1][2], int(communes_2021[i + 1][5])] for i in range(len(communes_2021) - 1)]

# Lecture des métadonnées sur les communes
communes = []
with open('metadonnees_communes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        communes.append(row)

communes = [[communes[i + 118][2], communes[i + 118][3]] for i in range(len(communes) - 121)]

# Lecture des données de population pour 2008
communes_2008 = []
with open('donnees_2008.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        communes_2008.append(row)

communes_2008 = [[communes_2008[i + 1][2] + communes_2008[i + 1][5], int(communes_2008[i + 1][9])] for i in
                 range(len(communes_2008) - 1)]

# Lecture des données de population pour 2016
communes_2016 = []
with open('donnees_2016.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        communes_2016.append(row)

communes_2016 = [[communes_2016[i + 1][2] + communes_2016[i + 1][5], int(communes_2016[i + 1][9])] for i in
                 range(len(communes_2016) - 1)]

# Extraction des données pour Auxerre et Sens
A = 0
S = 0
for i in range(len(communes)):
    if communes[i][1] == 'Auxerre':
        A = communes[i][0]
    if communes[i][1] == 'Sens':
        S = communes[i][0]

# Remplacer les données pour Sens par les données des villes spécifiées
villes_specifiees = ["Appoigny", "Augy", "Bleigny-le-Carreau", "Branches", "Champs-sur-Yonne", "Charbuy",
                     "Chevannes", "Chitry", "Coulanges-la-Vineuse", "Escamps", "Escolives Sainte-Camille", "Gurgy",
                     "Gy-l'Evêque", "Irancy", "Jussy", "Lindry", "Monéteau", "Montigny-la-Resle", "Perrigny", "Quenne",
                     "Saint-Bris-le-Vineux", "Saint-Georges-sur-Baulche", "Vallan", "Venoy", "Villefargeau",
                     "Villeneuve-Saint-Salves", "Vincelles", "Vincelottes"]

donnees_S = [0, 0, 0]  # Placeholder pour les données de Sens
for i in range(len(communes)):
    if len(communes[i]) > 4 and communes[i][1] in villes_specifiees:
        donnees_S = [communes[i][2], communes[i][3], communes[i][4]]

# Collecte des données de population pour Auxerre et Sens
C = [[] for i in range(400)]
for i in range(33800, 34200):
    C[i - 33800] = communes[i]
    c = C[i - 33800][0]
    for j in range(len(communes_2008)):
        if communes_2008[j][0] == c:
            C[i - 33800] = C[i - 33800] + [communes_2008[j][1]]
    for j in range(len(communes_2016)):
        if communes_2016[j][0] == c:
            C[i - 33800] = C[i - 33800] + [communes_2016[j][1]]
    for j in range(len(communes_2021)):
        if communes_2021[j][0] == c:
            C[i - 33800] = C[i - 33800] + [communes_2021[j][1]]

# Extraction des données pour Auxerre
A_pop = []
for i in range(len(C)):
    if C[i][0] == A:
        A_pop = [C[i][2], C[i][3], C[i][4]]

# Extraction des données pour les villes spécifiées
S_pop = donnees_S

# Dates pour le traçage
dates = [2008, 2016, 2021]

# Traçage des données
plt.plot(dates, A_pop, color='b', label='Auxerre')
plt.plot(dates, S_pop, color='r', label='Villes spécifiées')
plt.scatter(dates, A_pop, color='b')
plt.scatter(dates, S_pop, color='r')
plt.title("Population à Auxerre et Villes spécifiées")
plt.ylabel('Population')
plt.xlabel('Années')
plt.legend()
plt.show()

# Traçage avec régression linéaire jusqu'en 2050
dates_new = [2008, 2050]

plt.scatter(dates, A_pop, color='b', label='Auxerre')
plt.scatter(dates, S_pop, color='r', label='Villes spécifiées')
plt.title("Population à Auxerre et Villes spécifiées")
plt.ylabel('Population')
plt.xlabel('Années')

# Régression linéaire pour Auxerre
coefA = np.polyfit(dates, A_pop, 1)
poly1d_fnA = np.poly1d(coefA)
plt.plot(dates_new, poly1d_fnA(dates_new), color='b', linestyle='dashed', label='Régression linéaire (Auxerre)')

# Régression linéaire pour les villes spécifiées
coefS = np.polyfit(dates, S_pop, 1)
poly1d_fnS = np.poly1d(coefS)
plt.plot(dates_new, poly1d_fnS(dates_new), color='r', linestyle='dashed', label='Régression linéaire (Villes spécifiées)')

plt.legend()
plt.show()

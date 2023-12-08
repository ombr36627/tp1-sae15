import csv
from matplotlib import pyplot as plt

# Charger les données de population d'Auxerre (2021)
auxerre_pop = []
with open('donnees_2021.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        auxerre_pop.append(row)

# Sélectionner les colonnes pertinentes (nom de la commune et population)
auxerre_pop = [[auxerre_pop[i + 1][2], int(auxerre_pop[i + 1][5])] for i in range(len(auxerre_pop) - 1)]

# Créer une liste pour la population d'Auxerre
auxerre_populations = [entry[1] for entry in auxerre_pop]

# Charger les données de population d'Auxerre (2008)
communes_2008 = []
with open('donnees_2008.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        communes_2008.append(row)

# Sélectionner les colonnes pertinentes pour 2008
communes_2008 = [[communes_2008[i + 1][2] + communes_2008[i + 1][5], int(communes_2008[i + 1][9])] for i in
                range(len(communes_2008) - 1)]

# Charger les données de population d'Auxerre (2016)
communes_2016 = []
with open('donnees_2016.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        communes_2016.append(row)

# Sélectionner les colonnes pertinentes pour 2016
communes_2016 = [[communes_2016[i + 1][2] + communes_2016[i + 1][5], int(communes_2016[i + 1][9])] for i in
                range(len(communes_2016) - 1)]

# Créer une liste pour les années correspondantes
dates = ['2008', '2016', '2021']

# Créer une liste pour les populations correspondantes
populations = [communes_2008[0][1], communes_2016[0][1], auxerre_populations[-1]]

# Tracer le graphique à barres
plt.bar(dates, populations, color=['blue', 'green', 'red'])

# Ajouter un titre et des labels d'axe
plt.title("Évolution de la population à Auxerre (2008-2021)")
plt.ylabel('Population')
plt.xlabel('Années')

# Afficher le graphique
plt.show()

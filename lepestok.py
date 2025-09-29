import csv
import matplotlib.pyplot as plt

with open('iris_data.csv') as f:
    reader = csv.DictReader(f)
    species = []
    petals = []
    for row in reader:
        species.append(row['Species'])
        petals.append(float(row['PetalLengthCm']))

# Подсчёт видов
species_counts = {}
for s in species:
    species_counts[s] = species_counts.get(s, 0) + 1

# Подсчёт по длине лепестка
c1 = sum(1 for x in petals if x > 1.2)
c2 = sum(1 for x in petals if 1.2 < x < 1.5)
c3 = sum(1 for x in petals if x > 1.5)

fig, axs = plt.subplots(1, 2, figsize=(14,6))
axs[0].pie(species_counts.values(), labels=species_counts.keys(), autopct='%1.1f%%', startangle=90)
axs[0].set_title('Виды ирисов')
axs[1].pie([c1, c2, c3], labels=['>1.2', '>1.2 и <1.5', '>1.5'], autopct='%1.1f%%', startangle=90)
axs[1].set_title('Длина лепестка')

plt.show()
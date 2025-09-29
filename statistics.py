import csv
import numpy as np
import matplotlib.pyplot as plt

def linear_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # коэффициент наклона (b1)
    b1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
    # свободный член (b0)
    b0 = y_mean - b1 * x_mean
    
    return b0, b1

# Читаем данные
with open('iris_data.csv', newline='') as f:
    reader = csv.DictReader(f)
    SepalLengthCm = []
    SepalWidthCm = []
    PetalLengthCm = []
    PetalWidthCm = []
    for row in reader:
        SepalLengthCm.append(float(row['SepalLengthCm']))
        SepalWidthCm.append(float(row['SepalWidthCm']))
        PetalLengthCm.append(float(row['PetalLengthCm']))
        PetalWidthCm.append(float(row['PetalWidthCm']))

data = {
    'SepalLengthCm': np.array(SepalLengthCm),
    'SepalWidthCm': np.array(SepalWidthCm),
    'PetalLengthCm': np.array(PetalLengthCm),
    'PetalWidthCm': np.array(PetalWidthCm)
}

pairs = [
    ('SepalLengthCm', 'SepalWidthCm'),
    ('SepalLengthCm', 'PetalLengthCm'),
    ('SepalLengthCm', 'PetalWidthCm'),
    ('SepalWidthCm', 'PetalLengthCm'),
    ('SepalWidthCm', 'PetalWidthCm'),
    ('PetalLengthCm', 'PetalWidthCm')
]

fig, axs = plt.subplots(2, 3, figsize=(18, 10))
axs = axs.flatten()

for i, (x_key, y_key) in enumerate(pairs):
    x = data[x_key]
    y = data[y_key]
    b0, b1 = linear_regression(x, y)
    y_pred = b0 + b1 * x
    
    axs[i].scatter(x, y, label='Данные')
    axs[i].plot(x, y_pred, color='red', label='Прямая МНК')
    axs[i].set_xlabel(x_key)
    axs[i].set_ylabel(y_key)
    axs[i].set_title(f'{y_key} от {x_key}\nКоэфф: {b1:.3f}, {b0:.3f}')
    axs[i].legend()

plt.tight_layout()
plt.show()

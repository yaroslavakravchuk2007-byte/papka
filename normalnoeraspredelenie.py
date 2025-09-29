import numpy as np
import matplotlib.pyplot as plt


samples = [10, 50, 500, 10000]


fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, n in enumerate(samples):
    data = np.random.normal(loc=0, scale=1, size=n)
    axes[i].hist(data, bins=20, color='skyblue', edgecolor='black')
    axes[i].set_title(f'n = {n}')
    axes[i].set_xlabel('Значение')
    axes[i].set_ylabel('Частота')

fig.suptitle('Гистограммы нормального распределения при увеличении размера выборки')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
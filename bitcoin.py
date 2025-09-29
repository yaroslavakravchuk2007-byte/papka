import csv
import matplotlib.pyplot as plt
from datetime import datetime

dates = []
close_prices = []

with open('BTC_data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        date_str = row[0]
        close_price = float(row[-1])
        dates.append(date_obj)
        close_prices.append(close_price)

plt.figure(figsize=(14,6))
plt.plot(dates, close_prices, label='Цена закрытия BTC')
plt.xlabel('Дата')
plt.ylabel('Цена закрытия')
plt.title('Исторический график цены биткоина')
plt.xticks(rotation=45)

plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%y'))

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

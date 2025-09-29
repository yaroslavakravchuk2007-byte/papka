import csv


data = [
    ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species'],
    [5.1, 3.5, 1.4, 0.2, 'Iris-setosa'],
    [4.9, 3.0, 1.4, 0.2, 'Iris-setosa'],
    [5.8, 2.7, 5.1, 1.9, 'Iris-virginica'],
    [6.7, 3.1, 4.7, 1.5, 'Iris-versicolor'],
    [5.6, 2.9, 3.6, 1.3, 'Iris-versicolor'],
]


with open('iris_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

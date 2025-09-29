import matplotlib.pyplot as plt
x_vals = [1,2,3,4]
y_vals = [1, 4, 6, 9]
plt.ylabel('Напряжение на вольтметре')
plt.xlabel('Сила тока на амперметре')
plt.plot(x_vals, y_vals)
plt.show()
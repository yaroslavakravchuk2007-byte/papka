def nod_function (a, b):
    if b == 0: 
        return a
    else:
        return nod_function(b, a % b) 
num1 = 68
num2 = 4578
print(f"НОД чисел {num1} и {num2} равен: {nod_function(num1, num2)}") 

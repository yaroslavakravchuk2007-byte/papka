N = 45678
n = 7
digits = '0123456789abcdefghijklmnopqrstuvwxyz'
if n > len(digits):
    print('Выходите за рамки допустимых значений')
else:
    result = ''  
    number = N   
    while number > 0:
        result = digits[number % n] + result
        number //= n 
    print(result)  

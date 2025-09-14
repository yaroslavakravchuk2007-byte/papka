a = input().strip()      
x = len(a)           
result = ''
b= x // 2
for i in range(0, x, b):
    group = a[i:i+b]
    result += group[::-1]

print(result)

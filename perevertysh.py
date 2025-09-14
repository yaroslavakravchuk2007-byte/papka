G = int(input())        
a = input().strip()      
x = len(a)
b = x // G               
result = ''

for i in range(0, x, b):
    group = a[i:i+b]
    result += group[::-1]

print(result)
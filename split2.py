a = input().strip()      
x = len(a)           
result = ''

for i in range(0, x, 2):
    group = a[i:i+2]
    result += group[::-1]

print(result)
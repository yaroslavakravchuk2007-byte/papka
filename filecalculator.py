with open("/Users/yaroslavakravchuk/Documents/python/input.txt", "r") as f:
    lines = f.read().splitlines()
a, b = map(int, lines[0].split())
znak = lines[1].strip()
if znak == '+':
    c = a + b
elif znak == '-':
    c = a - b
elif znak == '*':
    c = a * b
elif znak == '/':
    c = a / b
with open("/Users/yaroslavakravchuk/Documents/python/output.txt", "w") as f:
    f.write(str(c))
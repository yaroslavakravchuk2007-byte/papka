p= input()
i = 0
count = 0
while i < len(p):
    if p[i:i+3] == "...":
        count += 1
        i += 3
    elif p[i:i+2] == "?!":
        count += 1
        i += 2
    elif p[i:i+1] == ".":
        count += 1
        i += 1 
    else:
        i += 1

print(count)
m = int(input())

f = {}
starts = set()
ends = set()

for _ in range(m):
    a, b = input().split()
    f[a] = b
    starts.add(a)
    ends.add(b)

start = None
for x in starts:
    if x not in ends:
        start = x
        break

route = [start]
while start in f:
    start = f[start]
    route.append(start)

print(*route)
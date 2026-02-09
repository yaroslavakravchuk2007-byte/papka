from collections import deque

n, m = map(int, input().split())

g = {}
for i in range(n):
    g[i] = []

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)

s, t = map(int, input().split())

q = deque([s])
vis = {s}
ok = False

while q:
    x = q.popleft()
    if x == t:
        ok = True
        break
    for y in g[x]:
        if y not in vis:
            vis.add(y)
            q.append(y)

print("YES" if ok else "NO")
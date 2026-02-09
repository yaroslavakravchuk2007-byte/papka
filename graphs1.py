from collections import deque

m = int(input())
edges = []
nodes = set()

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    nodes.add(u)
    nodes.add(v)

# строим список соседей
g = {}
for x in nodes:
    g[x] = []

for u, v in edges:
    g[u].append(v)
    g[v].append(u)

if len(nodes) == 0:
    print("YES")
else:
    start = next(iter(nodes))
    q = deque([start])
    vis = {start}

    while q:
        x = q.popleft()
        for y in g[x]:
            if y not in vis:
                vis.add(y)
                q.append(y)

    print("YES" if len(vis) == len(nodes) else "NO")
import sys

m = int(input())
edges = []
nodes = set()

for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    nodes.add(u); nodes.add(v)

g = {}
for x in nodes:
    g[x] = []
for u, v in edges:
    g[u].append(v)
    g[v].append(u)

vis = set()

def dfs(v, parent):
    vis.add(v)
    for to in g[v]:
        if to not in vis:
            if dfs(to, v):
                return True
        elif to != parent:
            return True
    return False

cycle = False
for v in nodes:
    if v not in vis:
        if dfs(v, -1):
            cycle = True
            break

print("YES" if cycle else "NO")
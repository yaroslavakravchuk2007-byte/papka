import heapq

n, m = map(int, input().split())

g = {}
for i in range(n):
    g[i] = []

for i in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

s, t = map(int, input().split())

INF = 10**18
dist = [INF] * n
dist[s] = 0

pq = [(0, s)]

while pq:
    d, v = heapq.heappop(pq)
    if d != dist[v]:
        continue
    for to, w in g[v]:
        nd = d + w
        if nd < dist[to]:
            dist[to] = nd
            heapq.heappush(pq, (nd, to))

print(dist[t] if dist[t] != INF else -1)
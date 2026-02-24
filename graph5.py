from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dist = [-1] * n
dist[0] = 0

queue = deque([0])

while queue:
    node = queue.popleft()
    
    for neighbor in graph[node]:
        if dist[neighbor] == -1:
            dist[neighbor] = dist[node] + 1
            queue.append(neighbor)

for d in dist:
    print(d)
import heapq

V, E, start, end = input().split()
V = int(V)
E = int(E)

graph = {}

for _ in range(E):
    u, v, w = input().split()
    w = int(w)
    
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
        
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = {station: float('inf') for station in graph}
dist[start] = 0

pq = [(0, start)]

while pq:
    current_dist, node = heapq.heappop(pq)
    
    if current_dist > dist[node]:
        continue
        
    for neighbor, weight in graph[node]:
        new_dist = current_dist + weight
        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist
            heapq.heappush(pq, (new_dist, neighbor))

print(dist[end])
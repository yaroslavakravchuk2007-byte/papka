def dfs(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

N = int(input())
M = int(input())

graph = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * N
componenti = 0

for i in range(N):
    if not visited[i]:
        dfs(i)
        componenti += 1

print(componenti)
# спонсоры моих хороших оценок: я, чатик гпт, ребята с ФПМИ, а так же семинарский ноутбук
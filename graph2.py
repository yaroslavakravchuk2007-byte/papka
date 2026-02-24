def has_cycle(v, parent, visited, graph):
    visited[v] = True
    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            if has_cycle(neighbor, v, visited, graph):
                return True
        elif neighbor != parent:
            return True
    return False

V, E = map(int, input().split())
spisok = eval(input())  

visited = [False] * V
cycle_found = False

for i in range(V):
    if not visited[i]:
        if has_cycle(i, -1, visited, spisok):
            cycle_found = True
            break

if cycle_found:
    print("YES")
else:
    print("NO")
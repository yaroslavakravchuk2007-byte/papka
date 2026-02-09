from collections import deque

k = int(input())
words = [input().strip().lower() for _ in range(k)]

indeg = {}
outdeg = {}
und = {}   
used = set()

def add_key(d, key):
    if key not in d:
        d[key] = 0

def add_und(a, b):
    if a not in und:
        und[a] = set()
    if b not in und:
        und[b] = set()
    und[a].add(b)
    und[b].add(a)

for w in words:
    a = w[0]
    b = w[-1]
    add_key(indeg, a); add_key(indeg, b)
    add_key(outdeg, a); add_key(outdeg, b)

    outdeg[a] += 1
    indeg[b] += 1
    add_und(a, b)

    used.add(a); used.add(b)

ok = True
for v in used:
    if indeg[v] != outdeg[v]:
        ok = False

if ok and len(used) > 0:
    start = next(iter(used))
    q = deque([start])
    vis = {start}
    while q:
        x = q.popleft()
        for y in und.get(x, []):
            if y not in vis:
                vis.add(y)
                q.append(y)
    if vis != used:
        ok = False

print("YES" if ok else "NO")
# решение этой задачи спонсировали чат гпт премиум версия и умы с ФУПМА, за что им огромное спасибо, я не смогла придумать идеи для решения 
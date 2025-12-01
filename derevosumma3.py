def build(a, n):
    size = 1
    while size < n:
        size *= 2
    t = [0] * (2 * size)
    for i in range(n):
        t[size + i] = 1 if a[i] == 0 else 0
    for i in range(size - 1, 0, -1):
        t[i] = t[2 * i] + t[2 * i + 1]
    return t, size


def get(t, v, l, r, ql, qr):
    if ql <= l and r <= qr:
        return t[v]
    if r < ql or qr < l:
        return 0
    m = (l + r) // 2
    return get(t, 2 * v, l, m, ql, qr) + get(t, 2 * v + 1, m + 1, r, ql, qr)


def find_k(t, v, l, r, ql, qr, k):
    if l == r:
        return l
    m = (l + r) // 2
    left = get(t, 2 * v, l, m, ql, qr)
    if left >= k:
        return find_k(t, 2 * v, l, m, ql, qr, k)
    return find_k(t, 2 * v + 1, m + 1, r, ql, qr, k - left)



n = int(input())
a = list(map(int, input().split()))
m = int(input())
t, size = build(a, n)
res = []
for _ in range(m):
    l, r, k = map(int, input().split())
    l -= 1
    r -= 1
    idx = find_k(t, 1, 0, size - 1, l, r, k) + 1
    res.append(str(idx))
print(" ".join(res))



from math import gcd

n = int(input())
a = list(map(int, input().split()))
k = int(input())

lg = [0] * (n + 1)
for i in range(2, n + 1):
    lg[i] = lg[i // 2] + 1

p = lg[n] + 1
st = [[0] * n for _ in range(p)]

for i in range(n):
    st[0][i] = a[i]

j = 1
while j < p:
    ln = 1 << (j - 1)
    i = 0
    while i + (1 << j) <= n:
        st[j][i] = gcd(st[j - 1][i], st[j - 1][i + ln])
        i += 1
    j += 1

res = []
for _ in range(k):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    ln = lg[r - l + 1]
    g = gcd(st[ln][l], st[ln][r - (1 << ln) + 1])
    res.append(str(g))

print(" ".join(res))

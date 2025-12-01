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
        x = st[j - 1][i]
        y = st[j - 1][i + ln]
        st[j][i] = x if x > y else y
        i += 1
    j += 1

res = []
for _ in range(k):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    ln = lg[r - l + 1]
    x = st[ln][l]
    y = st[ln][r - (1 << ln) + 1]
    res.append(str(x if x > y else y))

print(" ".join(res))

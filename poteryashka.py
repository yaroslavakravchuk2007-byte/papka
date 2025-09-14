n,*m = map(int, input().split())
poteryashka = n * (n + 1) // 2 - sum(m)
print(poteryashka)

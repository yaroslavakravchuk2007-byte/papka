n, m = map(int, input().split())
mine = [list(map(int, input().split())) for _ in range(n)]


dp = [[[-10**9] * 3 for _ in range(m)] for _ in range(n)]


for d in range(3):
    dp[0][0][d] = mine[0][0]

moves = [(1, 0), (0, 1), (1, 1)]

for i in range(n):
    for j in range(m):
        for d in range(3):
            if dp[i][j][d] == -10**9:
                continue
            for nd in range(3):
                if nd == d:
                    continue
                ni, nj = i + moves[nd][0], j + moves[nd][1]
                if 0 <= ni < n and 0 <= nj < m:
                    dp[ni][nj][nd] = max(dp[ni][nj][nd], dp[i][j][d] + mine[ni][nj])

print(max(dp[n - 1][m - 1]))
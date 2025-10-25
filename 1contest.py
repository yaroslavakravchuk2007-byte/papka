def main():
   
    N, M = map(int, input().split())         
    x = list(map(int, input().split()))      
    y = list(map(int, input().split()))      

   
    dp = [0] * (M + 1) 

   
    for i in range(N):
        cost = x[i]
        syt = y[i]
        
        for w in range(M, cost - 1, -1):
            dp[w] = max(dp[w], dp[w - cost] + syt)

   
    print(dp[M])


if __name__ == "__main__":
    main()
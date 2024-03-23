m,n = [int(i) for i in input().split()]
c= int(input())

cursed = []
for _ in range(c):
    x,y = [int(i) for i in input().split()]
    cursed.append((x,y))

dp = [[0 for _ in range(n)] for _ in range(m)]

for i in range(0,m):
    for j in range(0,n):
        if (i,j) in cursed:
            dp[i][j] = 0
        else:
            if i==0 and j==0:
                dp[i][j] = 1
            elif i > 0 and j > 0:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]
print(dp[m-1][n-1])

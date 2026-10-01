import sys

def solve():
    data=sys.stdin.read().split()

    if not data:
        return

    m=int(data[0])
    n=int(data[1])

    if m==0 or n==0:
        print(0)
        return

    cost=[[0]*n for _ in range(m)]

    index=2

    for i in range(m):
        for j in range(n):
            cost[i][j]=int(data[index])
            index+=1

    dp=[[0]*n for _ in range(m)]    
    dp[0][0]=cost[0][0]

    for i in range(1,m):
        dp[i][0]=cost[i][0]+dp[i-1][0]
    for j in range(1,n):
        dp[0][j]=cost[0][j]+dp[0][j-1]

    for i in range(1,m):
        for j in range(1,n):
            if dp[i-1][j] < dp[i][j-1]:
                dp[i][j]=cost[i][j]+dp[i-1][j]
            else:
                dp[i][j]=cost[i][j]+dp[i][j-1]            
    print(dp[m-1][n-1])

if __name__ =="__main__":
    solve()    
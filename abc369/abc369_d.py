# 2次元dpを使う
# ここまで奇数体or偶数体　倒したという情報が必要だから
# t体目を倒すと、t+1に遷移するというイメージ


N=int(input())
A=[0]+[int(a) for a in input().split()]

dp=[[0,0] for _ in range(N+1)]
dp[1]=[0,A[1]]
for t in range(1,N):
    dp[t+1][0]=max(dp[t][0],dp[t-1][0],dp[t][1]+2*A[t+1],dp[t-1][1]+2*A[t+1])
    dp[t+1][1]=max(dp[t][0]+A[t+1],dp[t][1],dp[t-1][0]+A[t+1],dp[t-1][1])


print(max(dp[N]))

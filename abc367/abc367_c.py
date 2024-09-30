# i番目の要素が1以上R

N,K=map(int,input().split())
R=[int(r) for r in input().split()]


# 調べるパターン数は全部で5^N通り
# N重forループなので、再帰で実装

A=[]
def dfs(array):
    n=len(array)
    if n==N:
        if sum(array)%K==0:
            A.append(array)        
    else:
        for a in range(1,R[n]+1):
            dfs(array+[a])


dfs([])
for A_i in A:
    print(*A_i)
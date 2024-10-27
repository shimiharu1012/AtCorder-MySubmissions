# 一度も隣り合わなかった組数を求める
# 隣あった組数をsetでもって、引き算する
N,M=map(int,input().split())
adj_set=[]

for i in range(M):
    A=[int(a) for a in input().split()]
    for j in range(N-1):
        adj_set.append(tuple(sorted((A[j],A[j+1]))))

print((N*(N-1)//2)-len(set(adj_set)))
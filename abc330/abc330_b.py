# 範囲 全てのA_iに対して(1~N)、あるX_iを求める
# 条件　abs(X_i-A_i)<=abs(Y-A_i) (YはL<=Y<=Rの中で任意)

# N<200000
# R-Lは最大 10^9なので、素朴実装はTLE

# X_iは、L以上R以下の中で、A_iに最近の整数
# つまり、区間[L,R]の場所によって3通りに分けられる

N,L,R=map(int,input().split())
A=[int(a) for a in input().split()]
X=[]
for i in range(N):
    if R<A[i]:
        X.append(R)
    elif A[i]<L:
        X.append(L)
    else:
        X.append(A[i])

print(*X)
N=int(input())
# Aはあらかじめソートしておく
A=sorted([int(a) for a in input().split()])
Q=int(input())

def cond(x,target):
    return A[x]<target

def binary_sarch(target):
    ok,ng=0,N
    while ok+1<ng:
        mi=(ok+ng)//2
        if cond(mi,target):
            ok=mi
        else:
            ng=mi
    
    return ok+1

for i in range(Q):
    X=int(input())
    # Aにおいて、Xより小さい要素の個数を求める
    if A[-1]<X:
        print(N)
    elif A[0]>=X:
        print(0)
    else:
        # X未満の要素の個数を求める
        # X未満、X以上の境目を２分探索で求める
        
        print(binary_sarch(X))
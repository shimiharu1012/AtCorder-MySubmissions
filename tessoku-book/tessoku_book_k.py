N,X=map(int,input().split())
A=[int(a) for a in input().split()]

def cond(p):
    # 条件を書く
    # pがokか、ngか
    # pがok=  A[p]<=X
    # pがng=  A[X]<p
    return A[p]<=X



if A[-1]==X:
    print(N)
else:
    # XはA_0~A_N-2に存在する
    ok,ng=0,N
    
    while ok+1<ng:
        mi=(ok+ng)//2
        if cond(mi):
            ok=mi
        else:
            ng=mi

    print(ok+1)
# ソートしてから、プレゼントがおいてある座標について、その座標をスタートとする長さMの開区間にあるプレゼントの個数を調べる
# 具体的には、二分探索で、A[idx]>=x+Mとなるような最小のidxを求める

def cond(ub,idx):
    if A[idx]<ub:
        return True
    else:
        return False

N,M=map(int,input().split())
A=sorted([int(a) for a in input().split()])
ans=0
for i in range(N):
    x=A[i]
    ok=i
    ng=N
    while ok+1<ng:
        mid=(ok+ng)//2
        if cond(x+M,mid):
            ok=mid
        else:
            ng=mid

    if ans<(ok-i+1):
        ans=(ok-i+1)

print(ans)
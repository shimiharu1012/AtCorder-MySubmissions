import math
# 2分探索を使う
# N=2*10000^5なので、2分探索を使う

N,M=map(int,input().split())
A=[int(a) for a in input().split()]
# A=sorted([int(a) for a in input().split()])


def cond(x):
    # xがokかngかを調べる
    # min(X,A1)+min(x,A2)+...+min(x,A_N)<=Mになるか否かを調べる
    s=sum(min(x,a) for a in A)
    return s<=M


if sum(A)<=M:
    print("infinite")
else:
    # xはこの中にある
    # [ok,ng)　の区間を２分探索で狭めたい
    ok,ng=0,max(A)

    # xは0以上A_N未満になる
    # したがって、2分探索で狭める
    while ok+1<ng:
        mi=(ok+ng)//2
        if cond(mi):
            ok=mi
        else:
            ng=mi
    print(ok)


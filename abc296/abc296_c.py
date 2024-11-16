# Aはソートした方が良い
# X>=0
# Aiを固定した上で、
# Ai-Aj<=Xとなるような最大のjを求める
# このi,jに対して、Ai-Aj=Xなら終了
# X<=0
# Ai-Aj>=Xとなるような最小のi
# Ai-Ajだけでなく、Aj-Aiも考える


N,X=map(int,input().split())
if X<0:
    X*=-1
A=sorted([int(a) for a in input().split()],reverse=True)

def cond(A_i,p):
    return A_i-A[p]<=X


def f():
    for i in range(N):
        ok=i
        ng=N

        while ok+1<ng:
            mid=(ok+ng)//2
            if cond(A[i],mid):
                ok=mid
            else:
                ng=mid
        
        j=ok

        if A[i]-A[j]==X:

            return True


    return False




print("Yes" if f() else "No")
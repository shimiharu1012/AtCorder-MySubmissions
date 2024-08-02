# T_i/S_i=国iの通貨と国i+1の通貨の交換レート

# 交換できる通貨を交換する
# 交換できる通貨のうち、交換レートがひ
# 通貨の交換は一方行に行われる
# 硬貨がなるべく余らないように交換する


N=int(input())
A=[int(a) for a in input().split()]
for i in range(N-1):
    S,T=map(int,input().split())
    x=A[i]//S
    if x>0:
        A[i]-=S*x
        A[i+1]+=T*x


print(A[-1])
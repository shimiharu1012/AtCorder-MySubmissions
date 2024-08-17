# N<2x10^5
# したがって、素朴な実装ではTLEする

N=int(input())
_A=[int(a) for a in input().split()]
A=sorted(_A)+[10**7]

D={}
# D{Ai: sum...} Ai以下の要素全ての和を求める
# 配列を舐める操作一回でこれを行いたい
i=0
s=0
while True:
    s+=A[i]
    if A[i+1]>A[i]:
        D[A[i]]=s

    i+=1
    if i==N:
        break

S=sum(_A)

for k in range(N):
    if k==N-1:
        print(S-D[_A[k]])
    else:    
        print(S-D[_A[k]],end=' ')

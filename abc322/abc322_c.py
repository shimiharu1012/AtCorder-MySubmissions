# N<N<2*10^5なので、単純な２重ループだとTLE
# 

N,M=map(int,input().split())
A=[int(a) for a in input().split()]
idx=0
for d in range(1,N+1):
    
    if d==A[idx]:
        print(0)
        idx+=1
    else:
        print(A[idx]-d)

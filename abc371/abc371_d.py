# 累積和っぽい？
import bisect

N=int(input())
X=[int(x) for x in input().split()]
P=[int(p) for p in input().split()]
# A=[A0,A1,A2...AN]とし、Aiは0番目の村からi番目の村に住む人の総数
A=[0]
for i in range(N):
    A.append(A[-1]+P[i])


Q=int(input())
ans=0
for _ in range(Q):
    ans=0
    L,R=map(int,input().split())
    

    l=bisect.bisect_left(X,L)
    r=bisect.bisect_right(X,R)
    
    print(A[r]-A[l])

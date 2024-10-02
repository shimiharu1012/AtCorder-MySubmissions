import bisect
# O(NxM)はダメ
# Aを固定するとき、Aに最も近いBを２分探索でもとめれば良い
N,M=map(int,input().split())
A=sorted([int(a) for a in input().split()])
B=sorted([int(b) for b in input().split()])


MIN=10**9
for i in range(N):
    if A[i]<=B[0]:
        MIN=min(abs(A[i]-B[0]),MIN)
    elif A[i]>=B[-1]:
        MIN=min(abs(A[i]-B[-1]),MIN)
    else:
        j=bisect.bisect_left(B,A[i])
        MIN=min(min(abs(A[i]-B[j-1]),abs(A[i]-B[j])),MIN)
    
print(MIN)
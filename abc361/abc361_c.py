from collections import deque

N,K=map(int,input().split())
A=[int(a) for a in input().split()]

A=sorted(A)

min=A[-1]-A[0]
for i in range(K+1):
    if (A[i+N-K-1]-A[i])<min:
        min=(A[-K+i-1]-A[i])


print(min)
        


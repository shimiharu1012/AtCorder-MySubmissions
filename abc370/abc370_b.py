N=int(input())
A=[]
for i in range(N):
    A.append([int(A_ij) for A_ij in input().split()])

e1=1
for t in range(1,N+1):
    e2=t
    e1=A[max(e1,e2)-1][min(e1,e2)-1]


print(e1)
    
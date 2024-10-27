N,M=map(int,input().split())
C=input().split()
D=input().split()
P=[int(p) for p in input().split()]
# D_P=[{"d":D[i],"price":P[i]} for i in range(M)]


cost=0
for i in range(N):
    if not C[i] in D:
        cost+=P[0]
    for j in range(M):
        if C[i]==D[j]:
            cost+=P[j+1]
            break
    

print(cost)
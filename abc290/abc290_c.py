N,K=map(int,input().split())
A=[int(a) for a in input().split()]

B=[False]*(K+1)

for i in range(N):
    if A[i]<=K:
        B[A[i]]=True

j=0
while j<K:
    if not B[j]:
        break
    j+=1

print(j)
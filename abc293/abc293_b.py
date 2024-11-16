N=int(input())
A=[0]+[int(a) for a in input().split()]
Called=[False]*(N+1)

for i in range(1,N+1):
    if not Called[i]:
        Called[A[i]]=True

print(N-sum(Called))
ans=[]
for i in range(1,N+1):
    if not Called[i]:
        ans.append(i)

print(*ans)
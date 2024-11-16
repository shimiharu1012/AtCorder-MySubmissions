
socks={}

N=int(input())
A=[int(a) for a in input().split()]

for i in range(N):
    if A[i] in socks:
        socks[A[i]]+=1
    else:
        socks[A[i]]=1

ans=0
for n in socks.values():
    ans+=n//2

print(ans)
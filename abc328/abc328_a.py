N,X=map(int,input().split())
S=[int(s) for s in input().split()]

ans=0
for s in S:
    if s<=X:
        ans+=s

print(ans)
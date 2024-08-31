N,K=map(int,input().split())
A=[int(a) for a in input().split()]

print(*[a//K for a in A if a%K==0],sep=' ')
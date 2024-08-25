N,K=map(int,input().split())
A=[int(a) for a in input().split()]

cutted=A[-K:]+A[:N-K]
print(*cutted,sep=' ')
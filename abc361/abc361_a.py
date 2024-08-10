N,K,X=map(int,input().split())
A=[int(a) for a in input().split()]

print(*(A[:K]+[X]+A[K:]))
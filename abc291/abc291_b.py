N=int(input())
X=sorted([int(x) for x in input().split()])

print(sum(X[N:-N])/(3*N))
